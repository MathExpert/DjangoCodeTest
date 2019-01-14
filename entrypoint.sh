#!/bin/bash

cd /opt/cloud_test_app

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --django-manage)
    MANAGE_COMMAND="python manage.py $2"
    eval $MANAGE_COMMAND
    shift # past argument
    shift # past value
    ;;
    --manage-shell)
    python manage.py shell -c "$2"
    shift # past argument
    shift # past value
    ;;
    --start-service)
    START_SERVICE=true
    shift # past argument
    ;;
    --hot-reload)
    HOT_RELOAD=true
    shift # past argument
    ;;
    *)
    shift # past unknown
    ;;
esac
done


# Start service
if [ "$START_SERVICE" = true ] || [ "$HOT_RELOAD" = true ]
then
  python startup_check.py
  STARTUP_CHECKS=$?

  # Start Gunicorn processes
  if [ "$STARTUP_CHECKS" == 0 ]
  then
    if [ "$HOT_RELOAD" = true ]
    then
      echo "Starting Gunicorn with hot reloading."
      exec gunicorn cloud_test.wsgi:application \
          -c /etc/cloud_test/conf.py --reload
    else
      echo "Starting Gunicorn."
      exec gunicorn cloud_test.wsgi:application \
          -c /etc/cloud_test/conf.py
    fi
  else
    echo "Startup checks failed, not starting Gunicorn."
  fi
fi
