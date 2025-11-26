def can_shutdown(apps_closed, files_saved, internet_disconnected):
    """
    Checks whether all required conditions to shut down are met.
    Returns True if ready, otherwise False.
    """
    if apps_closed and files_saved and internet_disconnected:
        return True
    else:
        return False
print("Shutdown Checklist:")
apps_closed = input("Have you closed all apps? (yes/no): ").lower() == "yes"
files_saved = input("Have you saved all your files? (yes/no): ").lower() == "yes"
internet_disconnected = input("Have you disconnected from the internet? (yes/no): ").lower() == "yes"
if can_shutdown(apps_closed, files_saved, internet_disconnected):
    print("\nYes, you can shut down the computer!")
else:
    print("\nSorry, you cannot shut down yet. Please complete all steps.")