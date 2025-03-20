# locators.py

# Application
APP = "Aliases.BookTicketsButton"

# Login Page
LOGIN_BUTTON = f"{APP}.UserLogin.RootPane.null_layeredPane.Panel.Button"

# Booking Panel
BOOKING_PANEL = f"{APP}.SwingObject('Add', 'Booking Panel', 0)"
BOOKING_TEXTAREA = f"{APP}.Add_.RootPane.null_layeredPane.Panel.TextArea"
DAY_RADIO_BUTTON = f"{APP}.Add_.RootPane.null_layeredPane.Panel.SwingObject('JRadioButton', 'Day', 0)"
ADD_BUTTON = f"{APP}.Add_.RootPane.null_layeredPane.Panel.SwingObject('JButton', 'Add', 0)"

# Confirmation Dialog
CONFIRM_BUTTON = f"{APP}.Dialog.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button"

# Success Popup
SUCCESS_LABEL = f"{APP}.SuccessPopup.RootPane.null_layeredPane.null_contentPane.OptionPane.Panel.OptionPane_realBody.OptionPane_body.OptionPane_label"
SUCCESS_OK_BUTTON = f"{APP}.SuccessPopup.RootPane.OptionPane_button"