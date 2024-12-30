import pyautogui
import time
import keyboard


def run_program(email_quantity= 1000, time_delay= 0.5):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
          "\nMAKE SURE YOUR ARE NOT IN YOUR PRIMARY EMAIL SECTION"
          "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
          "\nMay need to adjust time delay depending on wifi speed")

    box_coordinates = find_coordinates("check all checkbox")
    print(f"Coordinates for the checkbox: {box_coordinates}")
    time.sleep(3)
    delete_coordinates = find_coordinates("delete button")
    print(f"Coordinates for the delete button: {delete_coordinates}")

    #print("box_coordinates: ", box_coordinates)
    #print("delete_coordinates: ", delete_coordinates)
    delete_loop(box_coordinates, delete_coordinates, email_quantity, time_delay)


def find_coordinates(input_string):
    print(f"Move your mouse to the {input_string} and press the spacebar to stop the program.")

    try:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()
            print(f"Mouse Position: {x}, {y}", end="\r")  # Overwrites the same line

            # Check if the spacebar is pressed
            if keyboard.is_pressed('space'):
                break
    except KeyboardInterrupt:
        print("\nProgram stopped.")

    print("\nProgram stopped.")
    return x, y


def delete_loop(checkbox_position, delete_button_position, how_many_emails, time_delay):
    # Define the coordinates where the mouse should click
    # You can use pyautogui.position() to find these coordinates manually
    #delete_button_position = (-1636, 161)  # Replace (x, y) with the coordinates of the delete button
    #checkbox_position = (-1480, 163)  # Replace (x, y) with the checkbox for selecting emails

    # Number of emails to delete in one batch
    batch_size = how_many_emails//50
    print("Drag Mouse to the top right hand corner of screen to exit in an emergency")
    try:
        for _ in range(batch_size):
            # Move to the checkbox and click
            pyautogui.moveTo(checkbox_position)
            pyautogui.click()

            # Move to the delete button and click
            pyautogui.moveTo(delete_button_position)
            pyautogui.click()

            # Wait before repeating the process
            time.sleep(time_delay)

            # Check if the spacebar is pressed
            if keyboard.is_pressed('space'):
                break

    except KeyboardInterrupt:
        print("Process interrupted by user.")

run_program()


