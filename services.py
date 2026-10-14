def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_statistics(students):
    if not students:
        return {
            "total_students": 0,
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0
        }
    
    scores = [s.Score for s in students]
    return {
        "total_students": len(students),
        "average_score": round(sum(scores) / len(scores), 2),
        "highest_score": max(scores),
        "lowest_score": min(scores)
    }