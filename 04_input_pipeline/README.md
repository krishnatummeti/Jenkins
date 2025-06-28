
# when

#  This stage will only execute if the environment variable DEPLOY_TO is exactly 'production' 
when {
    allOf {
        environment name: 'DEPLOY_TO', value: 'production'
    }
}

-----------------------------------------------------------------------------------------------