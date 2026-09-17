# Domain model

## User

Account identity, credentials hash, activity flags.

## Exercise

Named movement with optional muscle group and equipment.  
May be system-owned (`created_by=null`) or user-owned.

## Workout

Training session on a date, belonging to one user, containing ordered sets.

## WorkoutSet

Single set: exercise, set number, reps, weight, optional RPE.

## Progress

Derived read-model: totals, personal records, volume over time (not persisted as its own table).
