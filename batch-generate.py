from happytransformer import HappyGeneration
from happytransformer import GENSettings, GENTrainArgs
import argparse
import textwrap

def main(args):
    if args.from_model:
        model = HappyGeneration(load_path=args.from_model);
    else:
        model = HappyGeneration(model_type="GPT-NEO", model_name="EleutherAI/gpt-neo-125M");
        
    top_k_sampling_settings = GENSettings(do_sample=True,
                                          top_k=args.top_k,
                                          max_length=args.max_length,
                                          min_length=args.min_length);
    done = False;
    for i in range(args.number):
        p = args.prompt;
        print(i);
        if p != "xxx":
            output_top_k_sampling = model.generate_text(":::  "+p, args=top_k_sampling_settings)
            txt = output_top_k_sampling.text;
            parts = txt.split(":::");
            parts.reverse();
            parts = parts[1:];
            txt = "\n".join(parts);            
            with open(args.output,'a') as fpr:
                fpr.write(textwrap.fill(p+""+txt));
                fpr.write("\n**********\n".format());
        else:
            done = True;

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--from_model', default=False);
    parser.add_argument('-l', '--min_length', default=300, type=int);
    parser.add_argument('-x', '--max_length', default=500, type=int);
    parser.add_argument('-k', '--top_k', default=50, type=int);
    parser.add_argument('-p', '--prompt', default="AITA");
    parser.add_argument('-n', '--number', default=25, type=int);
    parser.add_argument('-o', '--output', default="generated-batch.txt");
    
    args = parser.parse_args()
    main(args)
