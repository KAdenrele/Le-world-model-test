import subprocess
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():

    logger.info("Starting training process.")
    train_command = ["python", "train.py", "data=pusht"]
    try:
        subprocess.run(train_command, check=True)
        logger.info("Training process completed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Training process failed: {e}")
        sys.exit(1)

    logger.info("Starting evaluation process.")
    eval_command = ["python", "eval.py", "--config-name=pusht", "policy=pusht/lewm_epoch_11"]
    try:
        subprocess.run(eval_command, check=True)
        logger.info("Evaluation process completed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Evaluation process failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
