using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Windows.Forms;
using System.Threading;
using System.Diagnostics;
using System.Drawing;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        Thread t1, t2, t3, t4;
        IPEndPoint ipPoint;
        Socket listenSocket, handler;

        string str1 = "КГР";
        string str2 = "Пульс";
        string str3 = "";
        string str4 = "ЭЭГ";

        private void Form1_Load(object sender, EventArgs e)
        {
            t1 = new Thread(KRG);
            t2 = new Thread(Pulse);
            t3 = new Thread(EEG);
            t4 = new Thread(Emotion);
            t1.Start();
            t2.Start();
            t3.Start();
            t4.Start();

            ipPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8005);
            listenSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            listenSocket.Bind(ipPoint);
            listenSocket.Listen(10);
            // Process.Start(@"C:\Users\Lab210\3D Objects\hackaton\Новая папка\webCamEmocognizer-masterFinal\DetectEmotion.py");
        }

        void KRG()
        {
            IPEndPoint ipPoint1 = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8006);
            Socket listenSocket1 = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            listenSocket1.Bind(ipPoint1);
            listenSocket1.Listen(10);
            while (true)
            {
                Socket handler1 = listenSocket1.Accept();
                // получаем сообщение
                StringBuilder builder1 = new StringBuilder();
                int bytes1 = 0; // количество полученных байтов
                byte[] data1 = new byte[256]; // буфер для получаемых данных

                do
                {
                    bytes1 = handler1.Receive(data1);
                    builder1.Append(Encoding.UTF8.GetString(data1, 0, bytes1));
                }
                while (handler1.Available > 0);

                str1 = builder1.ToString();
            }
        }

        void Pulse()
        {
            IPEndPoint ipPoint3 = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8007);
            Socket listenSocket3 = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            listenSocket3.Bind(ipPoint3);
            listenSocket3.Listen(10);
            while (true)
            {
                Socket handler3 = listenSocket3.Accept();
                // получаем сообщение
                StringBuilder builder3 = new StringBuilder();
                int bytes3 = 0; // количество полученных байтов
                byte[] data3 = new byte[256]; // буфер для получаемых данных

                do
                {
                    bytes3 = handler3.Receive(data3);
                    builder3.Append(Encoding.UTF8.GetString(data3, 0, bytes3));
                }
                while (handler3.Available > 0);

                str2 = builder3.ToString();
            }
        }

        void EEG()
        {
            IPEndPoint ipPoint2 = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8009);
            Socket listenSocket2 = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            listenSocket2.Bind(ipPoint2);
            listenSocket2.Listen(10);
            while (true)
            {
                Socket handler2 = listenSocket2.Accept();
                // получаем сообщение
                StringBuilder builder2 = new StringBuilder();
                int bytes2 = 0; // количество полученных байтов
                byte[] data2 = new byte[256]; // буфер для получаемых данных

                do
                {
                    bytes2 = handler2.Receive(data2);
                    builder2.Append(Encoding.UTF8.GetString(data2, 0, bytes2));
                }
                while (handler2.Available > 0);

                str4 = builder2.ToString();
            }
        }

        void Emotion()
        {
            IPEndPoint ipPoint4 = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8008);
            Socket listenSocket4 = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            listenSocket4.Bind(ipPoint4);
            listenSocket4.Listen(10);
            while (true)
            {
                Socket handler4 = listenSocket4.Accept();
                // получаем сообщение
                StringBuilder builder4 = new StringBuilder();
                int bytes4 = 0; // количество полученных байтов
                byte[] data4 = new byte[256]; // буфер для получаемых данных

                do
                {
                    bytes4 = handler4.Receive(data4);
                    builder4.Append(Encoding.UTF8.GetString(data4, 0, bytes4));
                }
                while (handler4.Available > 0);

                str3 = builder4.ToString();
            }
        }


        public Form1()
        {
            InitializeComponent();
            button6.Visible = false;
            button7.Visible = false;
            button8.Visible = false;
            button9.Visible = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            send("1");
            button6.Visible = true; button7.Visible = true; button8.Visible = true; button9.Visible = true;
            button6.Text = "Хороший"; button7.Text = "В горошек"; button8.Text = "Проросший"; button9.Text = "Засохший";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            send("2");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            send("3");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            send("4");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            send("5");
            button6.Visible = true; button7.Visible = true; button8.Visible = true; button9.Visible = true;
            button6.Text = "Рыбы"; button7.Text = "Корабли"; button8.Text = "Моряки"; button9.Text = "Водоросли";
        }




        private void button6_Click(object sender, EventArgs e)
        {
            if (button6.Text == "Хороший")
                send("6");
            else
                send("A");

            button6.Visible = false;
            button7.Visible = false;
            button8.Visible = false;
            button9.Visible = false;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (button7.Text == "В горошек")
                send("7");
            else
                send("B");

            button6.Visible = false;
            button7.Visible = false;
            button8.Visible = false;
            button9.Visible = false;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (button8.Text == "Проросший")
                send("8");
            else
                send("C");
            button6.Visible = false;
            button7.Visible = false;
            button8.Visible = false;
            button9.Visible = false;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (button8.Text == "Засохший")
                send("9");
            else
                send("D");
            button6.Visible = false;
            button7.Visible = false;
            button8.Visible = false;
            button9.Visible = false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (str2.Length == 6)
            {
                label1.Text = "КГР: " + str2.Substring(0, 3);// Substring str2[0..2];
                if (Convert.ToInt32(str2.Substring(0, 3)) < 280)
                {
                    label1.BackColor = Color.Red;
                }
                else
                {
                    if (Convert.ToInt32(str2.Substring(0, 3)) > 320)
                    {
                        label1.BackColor = Color.Red;
                    }
                    else
                    {
                        label1.BackColor = Color.Green;
                    }
                }

                label2.Text = "Пульс: " + str2.Substring(3, 3);
            }
            switch (str3)
            {
                case "[3]":
                    label3.Text = "Эмоция: Happy!!";
                    break;
                case "[0]":
                    label3.Text = "Эмоция: Angry";
                    break;
                case "[1]":
                    label3.Text = "Эмоция: Disgust";
                    break;
                case "[2]":
                    label3.Text = "Эмоция: Fear";
                    break;
                case "[4]":
                    label3.Text = "Эмоция: Sad";
                    break;
                case "[5]":
                    label3.Text = "Эмоция: Surprise";
                    break;
                default:
                    label3.Text = "Эмоция";
                    break;
            }
            label4.Text = str4;
            if (str4 == "0") 
                {
                label4.BackColor = Color.Red;
                }
                else
                {
                label4.BackColor = Color.Green;
                }

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        void send(string s)
        {
            handler = listenSocket.Accept();
            byte[] data = Encoding.Unicode.GetBytes(s);
            handler.Send(data);
            handler.Shutdown(SocketShutdown.Both);
            handler.Close();
        }
    }
}