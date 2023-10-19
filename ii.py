Downloading...
From: https://drive.google.com/uc?id=1LufhOF7wf92-wVUU0kkYsIaBM4Ho_6AV
To: /content/output_directory
100%|██████████| 1.34G/1.34G [00:17<00:00, 75.6MB/s]
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-2-044a9d13c416> in <cell line: 28>()
     36 
     37     # Train the model
---> 38     trainer.train(output_dir="output_directory")

<ipython-input-2-044a9d13c416> in train(self, output_dir)
     19     def train(self, output_dir: str = None):
     20         if output_dir:
---> 21             self.model_kwargs["suffix"] = output_dir
     22 
     23         self.model_kwargs["model"] = self.model_path

AttributeError: 'ArgillaOpenAITrainer' object has no attribute 'model_kwargs'