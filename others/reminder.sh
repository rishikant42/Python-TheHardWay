#!/bin/bash
cd ~/redmine/
bundle exec rake redmine:send_reminders RAILS_ENV="production"
