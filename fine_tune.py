from happytransformer import HappyGeneration
from happytransformer import GENSettings, GENTrainArgs

def main(args):
    if(args.starting_model):
        model = HappyGeneration.load(args.starting_model);
    else:
        model = HappyGeneration(model_type="GPT-NEO", model_name="EleutherAI/gpt-neo-125M")

    train_args = GENTrainArgs(num_train_epochs=args.epochs,
                              learning_rate=args.learning_rate,
                              batch_size=args.batch_size);
    model.train(args.training_file, args=train_args);
    model.save(args.output_dir);

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_dir');
    parser.add_argument('-t', '--training_file');
    parser.add_argument('-e', '--epochs', type=int, default=5);
    parser.add_argument('-l', '--learning_rate', type=float, default=2e-05);
    parser.add_argument('-b', '--batch_size', type=int, default=2);
    args = parser.parse_args()
    main(args)
