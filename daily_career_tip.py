import random


# List of career tips and motivational messages
career_tips = [
    "Do not be afraid to start small. Every career begins somewhere.",

    "Learn a new skill today that can help you tomorrow.",

    "Your first job does not have to be your final career.",

    "Ask questions. You can learn a lot from people with more experience.",

    "Build a portfolio of your work. It can speak for you when applying for jobs.",

    "Do not compare your career journey with someone else's.",

    "Mistakes are part of learning. Use them to improve.",

    "Networking is not only about getting jobs. It is also about building relationships.",

    "Be willing to learn, even when you think you already know enough.",

    "Good communication can be just as important as technical skills.",

    "Set small career goals and work on them consistently.",

    "Your skills become more valuable when you know how to use them to solve problems.",

    "Do not wait until you feel completely ready before trying something new.",

    "Take feedback seriously, but do not let criticism stop you from improving.",

    "Find something you enjoy and look for ways to become good at it.",

    "Consistency can take you further than motivation alone.",

    "Keep learning because the job market keeps changing.",
    
    "Believe in your ability to improve with practice."
]


def show_daily_tip():
  
    tip = random.choice(career_tips)

    print("=" * 55)
    print("              DAILY CAREER TIP")
    print("=" * 55)
    print()
    print(f"💡 {tip}")
    print()
    print("Have a productive day!")
    print("=" * 55)


if __name__ == "__main__":
    show_daily_tip()
