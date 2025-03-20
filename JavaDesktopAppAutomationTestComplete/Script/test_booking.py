# test_booking.py
import common_functions as cf
import BookTicket as bf

def test_book_ticket():
    """Test Case: Launch application, book a ticket, and verify success message, close the app."""
    cf.launch_application()
    bf.book_ticket()
    bf.verify_booking()
    cf.close_application()
    
def test_book_ticket1():
    """Test Case: Launch application, book a ticket, and verify success message, close the app."""
    cf.launch_application()
    bf.book_ticket()
    bf.verify_booking1()
    cf.close_application()

#Login using record script  
def Test1():
  TestedApps.railway.Run()
  java = Aliases.BookTicketsButton
  java.UserLogin.Button2.ClickButton()
  panel = java.AdminLogin.RootPane.null_layeredPane.Panel
  panel.TextField.SetText("Test")
  passwordField = panel.PasswordField
  passwordField.Click(119, 37)
  passwordField.SetText(Project.Variables.Password1)
  panel.Button.ClickButton()
  aqObject.CheckProperty(Aliases.BookTicketsButton.SuccessPopup.RootPane.OptionPane_label2, "Enabled", cmpEqual, True)
  java.SuccessPopup.RootPane.OptionPane_button.ClickButton()
