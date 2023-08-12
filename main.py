from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage04_model_trainer import ModelTrainingPipeline
from TextSummarizer.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<")
except Exception as e:
    logger.ecxeption(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<")
except Exception as e:
    logger.ecxeption(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<")
except Exception as e:
    logger.ecxeption(e)
    raise e


STAGE_NAME = "Model Training stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
    model = ModelTrainingPipeline()
    model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<")
except Exception as e:
    logger.ecxeption(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


