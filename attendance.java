import javax.swing.*;
import java.awt.event.*;
import java.sql.*;
import java.time.LocalDate;

public class AttendanceApp extends JFrame {
    private JTextField nameField;
    private JButton markButton;
public AttendanceApp() {
        setTitle("Attendance Management System");
        setSize(400, 150);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(null);

        JLabel nameLabel = new JLabel("Student Name:");
        nameLabel.setBounds(20, 20, 100, 25);
        add(nameLabel);
	nameField = new JTextField();
        nameField.setBounds(130, 20, 200, 25);
        add(nameField);

        markButton = new JButton("Mark Present");
        markButton.setBounds(130, 60, 150, 30);
        add(markButton);
