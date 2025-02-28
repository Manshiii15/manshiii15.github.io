if None not in [left_hip_angle, right_hip_angle, left_knee_angle, right_knee_angle, 
                left_elbow_angle, right_elbow_angle, left_shoulder_angle, right_shoulder_angle]:
    
    if current_stage == "start":
        if left_knee_angle < 150 and right_knee_angle < 150 and left_hip_angle < 165 and right_hip_angle < 165:
            feedback.append("Straighten your legs")
        elif left_shoulder_angle < 60 and right_shoulder_angle < 60 and left_elbow_angle < 170 and right_elbow_angle < 170:
            feedback.append("Straighten your hands")
        else:
            current_stage = "pushup_start"
            print("current_stage = pushup_start")

    elif current_stage == "pushup_start":
        if left_elbow_angle > 90 and right_elbow_angle > 90:
            feedback.append("Bend elbows more")
        elif left_shoulder_angle > 40 and right_shoulder_angle > 40:
            feedback.append("Tuck in your elbows")
        else:
            current_stage = "pushup_end"
            print("current_stage = pushup_end")

    elif current_stage == "pushup_end":
        if left_knee_angle < 150 and right_knee_angle < 150 and left_hip_angle < 165 and right_hip_angle < 165:
            feedback.append("Straighten your legs")
        elif left_shoulder_angle < 90 and right_shoulder_angle < 90 and left_elbow_angle < 170 and right_elbow_angle < 170:
            feedback.append("Straighten your hands")
        else:
            correct_exercise_count += 1
            current_stage = "start"