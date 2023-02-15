import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.BorderLayout;
import java.awt.Dimension;

import javax.swing.JLabel;
import javax.imageio.ImageIO;
import javax.swing.JButton;
import java.awt.GridLayout;
import java.io.File;
import java.io.IOException;

import com.github.sarxos.webcam.*;

public class Main extends JFrame {

	private JPanel Frame;
	JFrame window = new JFrame("Menu");
	private Webcam webcam = null;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main frame = new Main();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public JPanel create_topo() throws IOException {
		
		JPanel panel_topo = new JPanel();
		panel_topo.setPreferredSize( new Dimension( Frame.getWidth(), 450 ) );
		
//		webcam = Webcam.getDefault();
//		webcam.setViewSize(WebcamResolution.VGA.getSize());
//		webcam.open(true);
		
		//ImageIO.write(webcam.getImage(),"JPG", new File("firstCapture.jpg"));
		
		JLabel lblNewLabel = new JLabel("webcam");
		panel_topo.add(lblNewLabel);
		
		return panel_topo;
	}
	
	public JPanel create_centro() {
		JPanel panel_centro = new JPanel();
		panel_centro.setLayout(new BorderLayout(0, 0));
	
		int espacamento = 20;
		
		JPanel panel_esquerda = new JPanel();
		panel_esquerda.setPreferredSize( new Dimension( espacamento*4, panel_centro.getHeight() ) );
		panel_centro.add(panel_esquerda, BorderLayout.WEST);
		
		JPanel panel_direita = new JPanel();
		panel_direita.setPreferredSize( new Dimension( espacamento*4, panel_centro.getHeight() ) );
		panel_centro.add(panel_direita, BorderLayout.EAST);
		
		JPanel panel_cima = new JPanel();
		panel_cima.setPreferredSize( new Dimension( panel_centro.getWidth(),espacamento ) );
		panel_centro.add(panel_cima, BorderLayout.NORTH);
		
		JPanel panel_baixo = new JPanel();
		panel_baixo.setPreferredSize( new Dimension( panel_centro.getWidth(),espacamento ) );
		panel_centro.add(panel_baixo, BorderLayout.SOUTH);
		
		JPanel panel_meio = new JPanel();
		panel_meio.setLayout(new GridLayout(0, 3, 0, 0));
		
		JButton btn_inferência = new JButton("button inferência");
		panel_meio.add(btn_inferência);
		
		JPanel panel_beetwen = new JPanel();
		panel_meio.add(panel_beetwen);
		
		JButton btn_relatórios = new JButton("button relatórios");
		panel_meio.add(btn_relatórios);
		
		panel_centro.add(panel_meio, BorderLayout.CENTER);
		
		return panel_centro;
		
	}
	
	/**
	 * Create the frame.
	 * @throws IOException 
	 */
	public Main() throws IOException {
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 900, 600);
		
		Frame = new JPanel();
		Frame.setLayout(new BorderLayout(0, 0));
		setContentPane(Frame);
		
		JPanel panel_topo = create_topo();
		Frame.add(panel_topo, BorderLayout.NORTH);
		
		JPanel panel_centro = create_centro();
		Frame.add(panel_centro, BorderLayout.CENTER);	
		
		
	}

}
