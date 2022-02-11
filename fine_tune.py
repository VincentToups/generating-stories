from happytransformer import HappyGeneration
from happytransformer import GENSettings, GENTrainArgs
import argparse

def main(args):
    if(args.starting_model):
        model = HappyGeneration(load_path=args.starting_model);
    else:
        model = HappyGeneration(model_type=args.model_type, model_name=args.model_name)

    train_args = GENTrainArgs(num_train_epochs=args.epochs,
                              learning_rate=args.learning_rate,
                              batch_size=args.batch_size);
    model.train(args.training_file, args=train_args);
    model.save(args.output_dir);

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--starting_model', default=False);
    parser.add_argument('-o', '--output_dir');
    parser.add_argument('-t', '--training_file');
    parser.add_argument('-e', '--epochs', type=int, default=5);
    parser.add_argument('-l', '--learning_rate', type=float, default=2e-05);
    parser.add_argument('-b', '--batch_size', type=int, default=2);
    parser.add_argument('-T', '--model_type', default="GPT-NEO");
    parser.add_argument('-M', '--model_name', default="EleutherAI/gpt-neo-125M");
    args = parser.parse_args()
    main(args)
