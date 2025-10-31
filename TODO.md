# TODO List for Debugging Attendance Management System

## Step 1: Fix image capture loop in `take_img()` function
- Change 'pass' to 'break' when 'q' is pressed or sampleNum > 70. ✅

## Step 2: Fix database insertion in `Fillattendances()` (automatic attendance)
- Move DB insertion outside the face detection loop. ✅
- Insert all collected attendance records. ✅
- Handle `aa` as string (use aa[0] if array). ✅

## Step 3: Fix database insertion in `manually_fill()` function
- Ensure proper insertion for all records. ✅

## Step 4: Replace hardcoded paths with relative paths
- Update paths for directories like 'TrainingImage', 'StudentDetails', etc. ✅
- Update haarcascade paths to relative. ✅

## Step 5: Update `training.py` for consistency
- Ensure file filtering matches AMS_Run.py. ✅
- Update haarcascade path to relative. ✅

## Step 6: Test the fixes
- Run the app, take images, train model, fill attendance manually and automatically. ✅
