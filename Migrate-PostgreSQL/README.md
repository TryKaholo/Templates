# Migrate PostgreSQL Database

Migrate PostgreSQL Database template was designed to make migrating from Heroku to PostgreSQL or RDS (and vice versa) as easy as possible. For it to work, you just need to fill in the fields in the configuration.

Note: To get credentials for Heroku, go to your application page, Resources tab. You will see a list of your addons, select Heroku Postgres, on the Setting tab you will see a "View credentials" button.

### The description of the template works step by step:
* The first step dumps the database and stores it on the agent. Make sure PostgreSQL is installed on the agent and its version is equal to or higher than the version of PostgreSQL on the remote server.
* The second step, the agent uses the database dump to restore it on the remote server.

## Plugins used in the template
* [CommandLine](https://github.com/Kaholo/kaholo-plugin-cmd) Plugin for Kaholo
