# GCP Project Clean Up

When working on a pipeline, there are times when you have a project that you want to wipe clean. This helps for the testing and saves money for unused or testing resources.

## Requirements
The code layer MUST be edited for this pipeline to work properly
- The `DRY_RUN` variable is set to `true` by default. This way you know when you are deleting resources
- The `PROJECT_ID` needs to be filled with the project id of the project you wish to clean
- The `SECRET_KEY` is the value of the Service Account JSON file you will need to upload to the Kaholo Vault

If there are any missing resources you'd like us to add to this automation, please [contact our partner](https://kaholo.io/partners/jason-ribble) who created this pipeline
