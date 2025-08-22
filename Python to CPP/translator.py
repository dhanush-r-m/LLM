from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class CodeTranslator:
    def __init__(self , model_name = "bigcode/starcoder2-7b"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto" , torch_dtype = torch.float16)

    def translate(self,python_code:str) -> str:

        prompt = f"""# Task : Convert Python code to C++ code
        # Input : {python_code}
        # Output : """

        inputs = self.tokenizer(prompt, return_tensors= 'pt').to(self.model.device)
        outputs = self.model.generate(
            **inputs,
             max_new_tokens=1024,
             temperature = 0.2,
             do_sample = False
             )
        
        result = self.tokenizer.decode(outputs[0], skip_special_tokens = True)
        
        if "# C++ Code:" in result:
            return result.split("# C++ Code:")[1].strip()
        
        return result.strip()

