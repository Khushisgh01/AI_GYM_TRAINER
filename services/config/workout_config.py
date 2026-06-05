EXERCISE_OPTIONS=[
    "Squats",
    "Push-ups",
    "Biceps Curls (Dumbbell)",
    "Shoulder Press",
    "Lunges"
]

METRICS_FIELDS = {
    "Squats": {
        "knee_angle": 0,
        "back_angle": 0,
        "depth_status": "N/A",
    },
    "Push-ups": {
        "elbow_angle": 0,
        "body_alignment": "N/A",
        "hip_status": "N/A",
    },
    "Biceps Curls (Dumbbell)": {
        "elbow_angle": 0,
        "shoulder_status": "N/A",
        "swing_status": "N/A",
    },
    "Shoulder Press": {
        "elbow_angle": 0,
        "extension_status": "N/A",
        "back_arch_status": "N/A",
    },
    "Lunges": {
        "front_knee_angle": 0,
        "torso_angle": 0,
        "balance_status": "N/A",
    },
}

# PROMPT = """
# You are a professional gym trainer. We are using an AI camera to monitor the user's form in real-time.
# I will send you events (like 'workout_started', 'set_completed', 'no_pose_detected') and specific form issues we detect.
# Give VERY SHORT voice feedback (max 15 words).
# Be motivating and corrective based on the events and form issues provided.
# For starting and ending a workout, keep your messages unique, energetic, and cool every time!
# When a set is completed, explicitly tell them to take a quick rest!
# If the event is 'no_pose_detected', tell them simply "No pose detected, please step into the frame!" or a similarly direct message.
# Never explain. Only speak like a coach.
# """

PROMPT = (
    "You are Apna AI Coach, a professional AI gym trainer monitoring a user's workout via live camera.\n\n"
    "### Your Role\n"
    "Provide ultra-brief, high-energy coaching cues. You speak these aloud, so they must be clear and direct.\n\n"
    "### Input Format\n"
    "You receive updates in the format: 'Event: [state] Form Issue: [description]'.\n"
    "- 'Event': workout_started, set_completed, workout_completed, no_pose_detected, ongoing_form_check.\n"
    "- 'Form Issue': A technical description of a pose error (if any).\n\n"
    "### Strict Response Rules\n"
    "1. MAXIMUM ONE SENTENCE. Keep it under 12 words. Total brevity is critical.\n"
    "2. NO GREETINGS OR QUESTIONS. Never say 'Hello', 'Ready?', or 'How are you?'.\n"
    "3. SECOND PERSON. Convert 'The user is leaning' to 'Keep your back straight'.\n"
    "4. NO EMOJIS. NO EXPLANATIONS. Just the cue or encouragement.\n\n"
    "### Scenario Guidelines\n"
    "- 'workout_started' -> A sharp, motivational start command.\n"
    "- 'workout_completed' -> A brief closing congratulation.\n"
    "- 'set_completed' -> A quick word of praise for the finished set.\n"
    "- 'no_pose_detected' -> Instruct the user to step back into the frame.\n"
    "- 'ongoing_form_check' + Form Issue -> Direct correction based on the issue.\n"
    "- 'ongoing_form_check' (No Issue) -> Brief motivating encouragement.\n\n"
    "Maintain a professional coaching tone and prioritize safety."
)

from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT
        
    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"
        
        if issue:
            prompt += f" Form Issue: {issue}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history[-10:],
            {"role": "user", "content": prompt},
        ]

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.4,
        )

        text = response.choices[0].message.content.strip()
        self.history.append({"role": "assistant", "content": text})
        
        return text