from javax.swing import *
from java.awt import *
from javax.swing.table import DefaultTableModel
import login as l
import goadmin as ga
import gouser as gu
import gocontractor as gc
import godealer as gd
import registerUser as ru

#global fields to be used in different functions
frameA = JFrame("eConstruction")
frameU = JFrame("eConstruction")
frameC = JFrame("eConstruction")
frameD = JFrame("eConstruction")
frame1 = JFrame("Welcome to eConstruction")
frameS = JFrame("Register Yourself")
nameText = JTextField(10)
passText = JTextField(10)
nameTexts = JTextField(10)
nameTextus = JTextField(10)
passTexts = JTextField(10)
nameTextc = JTextField(10)
housetypeText = JTextField(10)
priceCont = JTextField(10)
locality = JTextField(10)

nameTextd = JTextField(10)
itemName = JTextField(10)
stock = JTextField(10)
priceDeal = JTextField(10)

userRb = JRadioButton("Normal User")
contractorRb = JRadioButton("Contractor")
dealerRb = JRadioButton("Hardware Dealer")
adminRb = JRadioButton("Admin")
nameSearchText = JTextField(10)
errorMsgL = JLabel("")
errorMsgS = JLabel("")
infoLabel = JTextArea("")

def addContDetails(event):
	bit = gc.updateDetails(nameTextc.getText(), housetypeText.getText(), locality.getText(),priceCont.getText())
	if bit == True:
		errorMsgL.setText("Updated Successfully")
		nameTextc.setText("")
		housetypeText.setText("")
		priceCont.setText("")
		locality.setText("")
	else:
		errorMsgL.setText("Unable to update!!")


def addDealDetails(event):
	bit = gd.updateDetails(nameTextd.getText(), itemName.getText(), stock.getText(),priceDeal.getText())
	if bit == True:
		errorMsgL.setText("Updated Successfully")
		nameTextd.setText("")
		itemName.setText("")
		stock.setText("")
		priceDeal.setText("")
	else:
		errorMsgL.setText("Unable to update!!")


#frame to be opened for Dealer
def frameDealer():
	#frameC = JFrame("eConstruction")
	frameD.setBounds(30,30,500,400)
	frameD.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frameD.setLayout(None)
	frameD.getContentPane().setBackground(Color.blue)
	
	welcomeLabel = JLabel("Welcome Dealer")
	welcomeLabel.setBounds(180,20,200,20)
	welcomeLabel.setForeground(Color.black)
	frameD.add(welcomeLabel)
	
	#name
	nameLabel = JLabel(" Enter Your Name : ")
	nameLabel.setBounds(90,60,200,20)
	nameLabel.setForeground(Color.black)
	frameD.add(nameLabel)
	nameTextd.setBounds(260,60,150,20)
	frameD.add(nameTextd)
	
	#houseType
	nameLabel = JLabel("Enter item name : ")
	nameLabel.setBounds(90,90,200,20)
	nameLabel.setForeground(Color.black)
	frameD.add(nameLabel)
	itemName.setBounds(260,90,150,20)
	frameD.add(itemName)
	
	#locality
	passLabel = JLabel("Enter quantity :")
	passLabel.setBounds(90,120,200,20)
	passLabel.setForeground(Color.black)
	frameD.add(passLabel)
	stock.setBounds(260,120,150,20)
	frameD.add(stock)

	#price
	passLabel = JLabel("Enter price :")
	passLabel.setBounds(90,150,200,20)
	passLabel.setForeground(Color.black)
	frameD.add(passLabel)
	priceDeal.setBounds(260,150,150,20)
	frameD.add(priceDeal)
	
	btnAddD = JButton("Add Details", actionPerformed = addDealDetails)
	btnAddD.setBounds(200, 200, 150, 20)
	frameD.add(btnAddD)

	btnLogout = JButton("Log Out", actionPerformed = logout)
	btnLogout.setBounds(200, 230, 150, 20)
	btnLogout.setBackground(Color.red)
	frameD.add(btnLogout)

	#label to show error messages
	#errorMsg = JLabel("")
	errorMsgL.setBounds(120, 260, 400, 30)
	errorMsgL.setForeground(Color.red)
	frameD.add(errorMsgL)
	errorMsgL.setText("")

	frameD.setVisible(True)


#frame to be opened for contractor
def frameContractor():
	#frameC = JFrame("eConstruction")
	frameC.setBounds(30,30,500,400)
	frameC.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frameC.setLayout(None)
	frameC.getContentPane().setBackground(Color.blue)
	
	welcomeLabel = JLabel("Welcome Contractor")
	welcomeLabel.setBounds(180,20,200,20)
	welcomeLabel.setForeground(Color.black)
	frameC.add(welcomeLabel)
	
	#name
	nameLabel = JLabel(" Enter Your Name : ")
	nameLabel.setBounds(90,60,200,20)
	nameLabel.setForeground(Color.black)
	frameC.add(nameLabel)
	nameTextc.setBounds(260,60,150,20)
	frameC.add(nameTextc)
	
	#houseType
	nameLabel = JLabel("Choose a house type : ")
	nameLabel.setBounds(90,90,200,20)
	nameLabel.setForeground(Color.black)
	frameC.add(nameLabel)
	housetypeText.setBounds(260,90,150,20)
	frameC.add(housetypeText)
	
	#locality
	passLabel = JLabel("Enter Locality :")
	passLabel.setBounds(90,120,200,20)
	passLabel.setForeground(Color.black)
	frameC.add(passLabel)
	locality.setBounds(260,120,150,20)
	frameC.add(locality)

	#price
	passLabel = JLabel("Enter price :")
	passLabel.setBounds(90,150,200,20)
	passLabel.setForeground(Color.black)
	frameC.add(passLabel)
	priceCont.setBounds(260,150,150,20)
	frameC.add(priceCont)
	
	btnAddc = JButton("Add Details", actionPerformed = addContDetails)
	btnAddc.setBounds(200, 200, 150, 20)
	frameC.add(btnAddc)

	btnLogout = JButton("Log Out", actionPerformed = logout)
	btnLogout.setBounds(200, 230, 150, 20)
	btnLogout.setBackground(Color.red)
	frameC.add(btnLogout)

	#label to show error messages
	#errorMsg = JLabel("")
	errorMsgL.setBounds(120, 260, 400, 30)
	errorMsgL.setForeground(Color.red)
	frameC.add(errorMsgL)
	errorMsgL.setText("")

	frameC.setVisible(True)

def showContractorDetails(event):
	ls = gu.dispContractorDetails()
	infoLabel.setText(None)
	errorMsgL.setText("")
	i = 0
	j = 1
	while i< len(ls):
		infoLabel.append(str(ls[i]))
		infoLabel.append(" ")
		n = j*9-1
		if i == n:
			j+=1
			infoLabel.append("\n")
		i+=1
	

def showDealerDetails(event):
	ls = gu.dispDealerDetails()
	infoLabel.setText(None)
	errorMsgL.setText("")
	i = 0
	j = 1
	while i< len(ls):
		infoLabel.append(str(ls[i]))
		infoLabel.append(" ")
		n = j*9-1
		if i == n:
			j+=1
			infoLabel.append("\n")
		i+=1
	

#frame to be opened for user
def frameUser():
	#frameU = JFrame("eConstruction")
	frameU.setBounds(30,30,500,400)
	frameU.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frameU.setLayout(None)
	frameU.getContentPane().setBackground(Color.blue)
	
	welcomeLabel = JLabel("Welcome User")
	welcomeLabel.setBounds(180,20,200,20)
	welcomeLabel.setForeground(Color.black)
	frameU.add(welcomeLabel)

	#buttons
	btnSingleuser = JButton("Contractor Details", actionPerformed = showContractorDetails)
	btnAllusers = JButton("Dealer Details", actionPerformed = showDealerDetails)
	btnSingleuser.setBounds(200, 100, 150, 20)
	btnAllusers.setBounds(200, 130, 150, 20)
	btnSingleuser.setBackground(Color.green)
	btnAllusers.setBackground(Color.green)
	frameU.add(btnSingleuser)
	frameU.add(btnAllusers)
	btnLogout = JButton("Log Out", actionPerformed = logout)
	btnLogout.setBounds(200, 160, 150, 20)
	btnLogout.setBackground(Color.red)
	frameU.add(btnLogout)

	#infoLabel = JTextArea("")
	infoLabel.setBounds(50,200,400,150)
	infoLabel.setLineWrap(True)
	infoLabel.setEditable(False)
	infoLabel.setText(None)
	frameU.add(infoLabel)
	
	#label to show error messages
	#errorMsg = JLabel("")
	errorMsgL.setBounds(120, 70, 400, 30)
	errorMsgL.setForeground(Color.red)
	frameU.add(errorMsgL)
	errorMsgL.setText("")

	frameU.setVisible(True)

#back button of signup frame
def backBtnClicked(event):
	frameS.getContentPane().removeAll()
	frameS.setVisible(False)
	firstFrame()

#sign up form validation
def formValidateS():
	c = False
	name = nameTexts.getText()
	uname = nameTextus.getText()
	passwd = passTexts.getText()
	if name == "" or uname == "" or passwd == "":
		c = False
	else:
		c = True
	return c

#on sign up submission btn clicked
def finalsignUpBtnClicked(event):
	name = nameTexts.getText()
	uname = nameTextus.getText()
	passwd = passTexts.getText()
	usertype = whichRB()
	if formValidateS():	
		bit = ru.registerUserfunc(name,uname,passwd,usertype)
		if bit == True:
			errorMsgS.setForeground(Color.black)
			errorMsgS.setText("successfully updated.")
			nameTexts.setText("")
			nameTextus.setText("")
			passwd.setText("")
		elif bit == False:
			errorMsgS.setForeground(Color.red)
			errorMsgS.setText("Some Error Occurred In Creating profile !")
	else:
		errorMsgS.setForeground(Color.red)
		errorMsgS.setText("Please Enter Details !")

#signup frame
def frameSignUp():
	frameS.setBounds(30,30,500,400)
	frameS.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frameS.setLayout(None)
	frameS.getContentPane().setBackground(Color.blue)
	
	welcomeLabel = JLabel("Enter Your Details")
	welcomeLabel.setBounds(180,20,200,20)
	welcomeLabel.setForeground(Color.black)
	frameS.add(welcomeLabel)

	#name
	nameLabel = JLabel(" Enter Your Name : ")
	nameLabel.setBounds(90,60,200,20)
	nameLabel.setForeground(Color.black)
	frameS.add(nameLabel)
	nameTexts.setBounds(260,60,150,20)
	frameS.add(nameTexts)
	
	#name
	nameLabel = JLabel("Choose a User Name : ")
	nameLabel.setBounds(90,90,200,20)
	nameLabel.setForeground(Color.black)
	frameS.add(nameLabel)
	nameTextus.setBounds(260,90,150,20)
	frameS.add(nameTextus)
	
	#password
	passLabel = JLabel("Create New Password :")
	passLabel.setBounds(80,120,200,20)
	passLabel.setForeground(Color.black)
	frameS.add(passLabel)
	passTexts.setBounds(260,120,150,20)
	frameS.add(passTexts)
	
	#radio buttons
	#userRb = JRadioButton("Normal User")
	userRb.setBounds(150, 180, 180, 20)
	userRb.setBackground(Color.blue)
	userRb.setForeground(Color.black)
	userRb.setSelected(True)
	#contractorRb = JRadioButton("Contractor")
	contractorRb.setBounds(150, 210, 180, 20)
	contractorRb.setBackground(Color.blue)
	contractorRb.setForeground(Color.black)
	#dealerRb = JRadioButton("Hardware Dealer")
	dealerRb.setBounds(150, 240, 180, 20)
	dealerRb.setBackground(Color.blue)
	dealerRb.setForeground(Color.black)

	# radio button group
	bG = ButtonGroup()
	bG.add(userRb)
	bG.add(dealerRb)
	bG.add(contractorRb)
	bG.add(adminRb)
	frameS.add(userRb)
	frameS.add(dealerRb)
	frameS.add(contractorRb)

	#login signup buttons
	btnLogin = JButton("Sign Up", actionPerformed = finalsignUpBtnClicked)
	btnSignup = JButton("Back", actionPerformed = backBtnClicked)
	btnLogin.setBounds(100, 300, 120, 30)
	btnSignup.setBounds(270, 300, 120, 30)
	btnLogin.setBackground(Color.green)
	btnSignup.setBackground(Color.green)
	frameS.add(btnLogin)
	frameS.add(btnSignup)

	#label to show error messages
	#errorMsg = JLabel("")
	errorMsgS.setBounds(120, 270, 400, 30)
	errorMsgS.setForeground(Color.red)
	frameS.add(errorMsgS)
	errorMsgS.setText("")

	#sign up frame
	frameS.setVisible(True)

#on sign up btn click
def signupBtnClicked(event):
	frame1.getContentPane().removeAll()
	frame1.setVisible(False)
	frameSignUp()

#logout btn
def logout(event):
	frameA.getContentPane().removeAll()
	frameA.setVisible(False)
	firstFrame()

#search for single user details in admin frame
def singleUserDetails(event):
	if nameSearchText.getText() == "":
		errorMsgL.setText("Please enter a user name")
	else:
		errorMsgL.setText("")
		infoLabel.setText(None)
		name = nameSearchText.getText()
		ls = ga.chkUser(name)
		i = 0
		j = 1
		while i< len(ls):
			infoLabel.append(str(ls[i]))
			infoLabel.append(" ")
			n = j*7-1
			if i == n:
				j+=1
				infoLabel.append("\n")
			i+=1

#get all user details in admin frame
def allUserDetails(event):
	infoLabel.setText(None)
	errorMsgL.setText("")
	ls = ga.allUsers()
	i = 0
	j = 1
	while i< len(ls):
		infoLabel.append(str(ls[i]))
		infoLabel.append(" ")
		n = j*7-1
		if i == n:
			j+=1
			infoLabel.append("\n")
		i+=1
		

#frame to be opened for admin
def frameAdmin():
	#frameA = JFrame("eConstruction")
	frameA.setBounds(30,30,500,400)
	frameA.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frameA.setLayout(None)
	frameA.getContentPane().setBackground(Color.blue)
	
	welcomeLabel = JLabel("Welcome Admin")
	welcomeLabel.setBounds(180,20,200,20)
	welcomeLabel.setForeground(Color.black)
	frameA.add(welcomeLabel)

	#student search field
	nameSearchLabel = JLabel("Enter name to search Details")
	#nameSearchText = JTextField(10)
	nameSearchLabel.setBounds(50, 50, 250, 20)
	nameSearchText.setBounds(280, 50, 150, 20)
	nameSearchLabel.setForeground(Color.black)
	nameSearchText.setForeground(Color.black)
	frameA.add(nameSearchText)
	frameA.add(nameSearchLabel)

	#buttons
	btnSingleuser = JButton("Show Details", actionPerformed = singleUserDetails)
	btnAllusers = JButton("All Users", actionPerformed = allUserDetails)
	btnSingleuser.setBounds(200, 100, 150, 20)
	btnAllusers.setBounds(200, 130, 150, 20)
	btnSingleuser.setBackground(Color.green)
	btnAllusers.setBackground(Color.green)
	frameA.add(btnSingleuser)
	frameA.add(btnAllusers)
	btnLogout = JButton("Log Out", actionPerformed = logout)
	btnLogout.setBounds(200, 160, 150, 20)
	btnLogout.setBackground(Color.red)
	frameA.add(btnLogout)

	#infoLabel = JTextArea("")
	infoLabel.setBounds(50,200,400,150)
	infoLabel.setLineWrap(True)
	infoLabel.setEditable(False)
	infoLabel.setText(None)
	frameA.add(infoLabel)
	
	#label to show error messages
	#errorMsg = JLabel("")
	errorMsgL.setBounds(120, 70, 400, 30)
	errorMsgL.setForeground(Color.red)
	frameA.add(errorMsgL)
	errorMsgL.setText("")

	frameA.setVisible(True)

#function to determine which radio button is selected
def whichRB():
	usertype = "none"
	if userRb.isSelected():
		usertype = "normal user"
	elif contractorRb.isSelected():
		usertype = "contractor"
	elif dealerRb.isSelected():
		usertype = "hardware dealer"
	elif adminRb.isSelected():
		usertype = "admin"
	return usertype

#from validation
def formValidate():
	bit = False
	name = nameText.getText()
	passwd = passText.getText()
	if name == "" or passwd == "":
		bit = False
		errorMsgL.setText("Please Enter Details !!")
	else:
		bit = True
	return bit

#on clicking login button
def loginBtnClicked(event):
	if formValidate():
		name = nameText.getText()
		passwd = passText.getText()
		usertype = whichRB()
		chk = l.signIn(name, passwd, usertype)
		print(chk)
		if chk == True:
			if usertype == "admin":
				frame1.getContentPane().removeAll()
				frame1.setVisible(False)
				frameAdmin()
			elif usertype == "normal user":
				frame1.getContentPane().removeAll()
				frame1.setVisible(False)
				frameUser()
			elif usertype == "contractor":
				frame1.getContentPane().removeAll()
				frame1.setVisible(False)
				frameContractor()
			elif usertype == "hardware dealer":
				frame1.getContentPane().removeAll()
				frame1.setVisible(False)
				frameDealer()

		elif chk == False:
			errorMsgL.setText("Username/Password mismatched !!")

#first frame
def firstFrame():	
	#frame1 = JFrame("Welcome to eConstruction")
	frame1.setBounds(30,30,500,400)
	frame1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frame1.setLayout(None)
	frame1.getContentPane().setBackground(Color.blue)
	
	#enter credential msg
	welcomeLabel = JLabel(" Enter Credentials ")
	welcomeLabel.setBounds(180,20,200,20)
	welcomeLabel.setForeground(Color.black)
	frame1.add(welcomeLabel)
	
	#name
	nameLabel = JLabel(" User Name : ")
	nameLabel.setBounds(90,60,200,20)
	nameLabel.setForeground(Color.black)
	frame1.add(nameLabel)
	nameText.setBounds(260,60,150,20)
	frame1.add(nameText)
	
	#password
	passLabel = JLabel(" Password : ")
	passLabel.setBounds(90,90,200,20)
	passLabel.setForeground(Color.black)
	frame1.add(passLabel)
	passText.setBounds(260,90,150,20)
	frame1.add(passText)
	
	#radio buttons
	#userRb = JRadioButton("Normal User")
	userRb.setBounds(150, 150, 180, 20)
	userRb.setBackground(Color.blue)
	userRb.setForeground(Color.black)
	userRb.setSelected(True)
	#contractorRb = JRadioButton("Contractor")
	contractorRb.setBounds(150, 180, 180, 20)
	contractorRb.setBackground(Color.blue)
	contractorRb.setForeground(Color.black)
	#dealerRb = JRadioButton("Hardware Dealer")
	dealerRb.setBounds(150, 210, 180, 20)
	dealerRb.setBackground(Color.blue)
	dealerRb.setForeground(Color.black)
	#adminRb = JRadioButton("Admin")
	adminRb.setBounds(150, 240, 180, 20)
	adminRb.setBackground(Color.blue)
	adminRb.setForeground(Color.black)

	# radio button group
	bG = ButtonGroup()
	bG.add(userRb)
	bG.add(dealerRb)
	bG.add(contractorRb)
	bG.add(adminRb)
	frame1.add(userRb)
	frame1.add(dealerRb)
	frame1.add(contractorRb)
	frame1.add(adminRb)

	#login signup buttons
	btnLogin = JButton("Login", actionPerformed = loginBtnClicked)
	btnSignup = JButton("SignUp", actionPerformed = signupBtnClicked)
	btnLogin.setBounds(150, 300, 80, 30)
	btnSignup.setBounds(250, 300, 120, 30)
	btnLogin.setBackground(Color.green)
	btnSignup.setBackground(Color.green)
	frame1.add(btnLogin)
	frame1.add(btnSignup)

	#label to show error messages
	#errorMsg = JLabel("")
	errorMsgL.setBounds(120, 117, 400, 30)
	errorMsgL.setForeground(Color.red)
	frame1.add(errorMsgL)
	errorMsgL.setText("")
	#show frame
	frame1.setVisible(True)
	
firstFrame()
