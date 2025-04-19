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
	 markButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                markAttendance(nameField.getText());
            }
        });
    }

    private void markAttendance(String studentName) {
        String url = "jdbc:mysql://localhost:3306/attendance_db";
        String user = "root";
        String password = ""; 

        String sql = "INSERT INTO attendance (student_name, date, status) VALUES (?, ?, ?)";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             PreparedStatement stmt = conn.prepareStatement(sql)) { 
		stmt.setString(1, studentName);
            stmt.setDate(2, Date.valueOf(LocalDate.now()));
            stmt.setString(3, "Present");

            int rowsInserted = stmt.executeUpdate();
            if (rowsInserted > 0) {
                JOptionPane.showMessageDialog(this, "Attendance marked for " + studentName);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error marking attendance.");
        }
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new AttendanceApp().setVisible(true);
        });
    }
}

