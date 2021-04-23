# Madison Fletcher
# 1868748
def fat_burning_heart_rate(age):
    bpm = (220 - age) * .70
    return bpm


def get_age():
    age = int(input())
    if 18 < age < 75:
        return age
    else:
        raise ValueError("Invalid age")


if __name__ == "__main__":
    try:
        age2 = get_age()
        print("Fat burning heart rate for a", age2, "year-old:", fat_burning_heart_rate(age2), "bpm")
    except ValueError:
        print("Invalid age.")
        print("Could not calculate heart rate info.")
        print()
