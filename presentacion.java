import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JLabel;

public class Presentacion extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					presentacion frame = new presentacion();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public presentacion() {
		setTitle("RECOMENDACIONES GAMES");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 613, 486);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBounds(10, 11, 577, 436);
		contentPane.add(panel);
		panel.setLayout(null);
		
		JButton btnPc = new JButton("PC");
		btnPc.setBounds(146, 54, 201, 59);
		panel.add(btnPc);
		
		JButton button = new JButton("Ps4");
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			}
		});
		button.setBounds(354, 54, 201, 59);
		panel.add(button);
		
		JButton button_1 = new JButton("Xbox One");
		button_1.setBounds(146, 124, 201, 59);
		panel.add(button_1);
		
		JButton button_2 = new JButton("Wii U");
		button_2.setBounds(354, 124, 201, 59);
		panel.add(button_2);
		
		JButton button_3 = new JButton("Ps3");
		button_3.setBounds(146, 194, 201, 59);
		panel.add(button_3);
		
		JButton button_4 = new JButton("Xbox 360");
		button_4.setBounds(354, 194, 201, 59);
		panel.add(button_4);
		
		JButton button_5 = new JButton("Wii");
		button_5.setBounds(146, 264, 201, 59);
		panel.add(button_5);
		
		JButton btnds = new JButton("Nintendo 3DS");
		btnds.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnds.setBounds(354, 264, 201, 59);
		panel.add(btnds);
		
		JLabel lblPlataforma = new JLabel("Plataforma");
		lblPlataforma.setBounds(330, 11, 52, 32);
		panel.add(lblPlataforma);
		
		JButton btnPsVita = new JButton("PS vita");
		btnPsVita.setBounds(146, 334, 201, 59);
		panel.add(btnPsVita);
		
		JButton btnDs = new JButton("Nintendo Ds");
		btnDs.setBounds(354, 334, 201, 59);
		panel.add(btnDs);
	
	}
	
	
	
	
	
	
}
