from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create teams
        teams = [
            {"name": "Marvel", "description": "Team Marvel"},
            {"name": "DC", "description": "Team DC"}
        ]
        db.teams.insert_many(teams)

        # Create users (superheroes)
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Create activities
        activities = [
            {"user": "spiderman@marvel.com", "activity": "Running", "duration": 30},
            {"user": "ironman@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "wonderwoman@dc.com", "activity": "Swimming", "duration": 60},
            {"user": "batman@dc.com", "activity": "Yoga", "duration": 40}
        ]
        db.activities.insert_many(activities)

        # Create leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 120}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"user": "spiderman@marvel.com", "workout": "Push-ups", "reps": 50},
            {"user": "ironman@marvel.com", "workout": "Sit-ups", "reps": 40},
            {"user": "wonderwoman@dc.com", "workout": "Squats", "reps": 60},
            {"user": "batman@dc.com", "workout": "Pull-ups", "reps": 30}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
