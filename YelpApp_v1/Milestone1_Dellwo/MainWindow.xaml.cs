using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Npgsql;

namespace Milestone1_Dellwo
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        public class Business
        {
            public string name { get; set; }

            public string state { get; set; }

            public string city { get; set; }

            public string zipcode { get; set; }

        }
        public MainWindow()
        {
            InitializeComponent();
            addState();
            addColumns2Grid();
        }

        private string buildConnectionString()
        {
            return "Host = localhost; Username = postgres; Database = milestone2test; password = Password";
        }
        private void addState()
        {
            using (var connection = new NpgsqlConnection(buildConnectionString()))
            {
                connection.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = connection;
                    cmd.CommandText = "SELECT distinct y_state FROM business ORDER BY y_state";
                    try
                    {
                        var reader = cmd.ExecuteReader();
                        while (reader.Read())
                            state_list.Items.Add(reader.GetString(0));
                    }
                    catch (NpgsqlException ex)
                    {
                        Console.WriteLine(ex.Message.ToString());
                        System.Windows.MessageBox.Show("SQL Error - " + ex.Message.ToString());
                    }
                    finally
                    {
                        connection.Close();
                    }
                }
            }
            /*state_list.Items.Add("WA");
            state_list.Items.Add("CA");
            state_list.Items.Add("ID");
            state_list.Items.Add("NV");*/
        }

        private void addColumns2Grid()
        {
            DataGridTextColumn col1 = new DataGridTextColumn();
            col1.Binding = new Binding("name");
            col1.Header = "BusinessName";
            col1.Width = 255;
            business_grid.Columns.Add(col1);

            DataGridTextColumn col2 = new DataGridTextColumn();
            col2.Binding = new Binding("state");
            col2.Header = "State";
            col2.Width = 50;
            business_grid.Columns.Add(col2);

            DataGridTextColumn col3 = new DataGridTextColumn();
            col3.Binding = new Binding("city");
            col3.Header = "City";
            col3.Width = 180;
            business_grid.Columns.Add(col3);


            DataGridTextColumn col4 = new DataGridTextColumn();
            col4.Binding = new Binding("zipcode");
            col4.Header = "Zipcode";
            col4.Width = 100;
            business_grid.Columns.Add(col4);

            /*business_grid.Items.Add(new Business() { name = "Business 1", state = "WA", city = "Pullman" });
            business_grid.Items.Add(new Business() { name = "Business 2", state = "CA", city = "Arcata" });
            business_grid.Items.Add(new Business() { name = "Business 3", state = "NV", city = "Reno" });*/

        }

        private void execute_query(string sqlstr, Action<NpgsqlDataReader> myf)
        {
            using (var connection = new NpgsqlConnection(buildConnectionString()))
            {
                connection.Open();
                using (var cmd = new NpgsqlCommand())
                {
                    cmd.Connection = connection;
                    cmd.CommandText = sqlstr;

                    try
                    {
                        var reader = cmd.ExecuteReader();
                        while (reader.Read())
                            myf(reader);
                    }
                    catch (NpgsqlException ex)
                    {
                        Console.WriteLine(ex.Message.ToString());
                        System.Windows.MessageBox.Show("Sql error: " + ex.Message.ToString());
                    }
                    finally
                    {
                        connection.Close();
                    }
                }
            }
        }



       




        private void state_list_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            City_list_box.Items.Clear();
            if (state_list.SelectedIndex > -1)
            {
                string sqlStr = "SELECT distinct y_city FROM business WHERE y_state = '" + state_list.SelectedItem.ToString() + "' ORDER BY y_city";
                execute_query(sqlStr, addCity);
            }
        }


        private void addGridRow(NpgsqlDataReader R)
        {
            Business item = new Business() { name = R.GetString(0), state = R.GetString(1), city = R.GetString(2), zipcode = R.GetString(3) };
            if (! (business_grid.Items.Contains(item.state)))//Does not do what we want.
            {
                business_grid.Items.Add(item);
            }
           // business_grid.Items.Add(new Business() { name = R.GetString(0), state = R.GetString(1), city = R.GetString(2), zipcode = R.GetString(3) });
        }

        private void addCategory(NpgsqlDataReader R)
        {
            Cat_list_box.Items.Add(R.GetString(0));
        }

        private void addCity(NpgsqlDataReader R)
        {
            City_list_box.Items.Add(R.GetString(0));
        }

        private void addZipcode(NpgsqlDataReader R)
        {
            Zipcode_list_box.Items.Add(R.GetString(0));
        }




      /*  private void city_list_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            business_grid.Items.Clear();
            if (city_list.SelectedIndex > -1)
            {
                string sqlStr = "SELECT name, state, city FROM business WHERE state = '" + state_list.SelectedItem.ToString() + "' AND city = '" + city_list.SelectedItem.ToString() + "' ORDER BY name";
                execute_query(sqlStr, addGridRow);
            }
        }*/

        private void City_list_box_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            Zipcode_list_box.Items.Clear();
            if(City_list_box.SelectedIndex > -1)
            {
                string sqlStr = "SELECT DISTINCT y_zipcode FROM business WHERE y_state = '" + state_list.SelectedItem.ToString() + "' AND y_city = '" + City_list_box.SelectedItem.ToString() + "' ORDER BY y_zipcode";
                execute_query(sqlStr, addZipcode);
            }



        }

        private void Zipcode_list_box_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            Cat_list_box.Items.Clear();
            business_grid.Items.Clear();
            if (Zipcode_list_box.SelectedIndex > -1)
            {

                string sqlStr = "Select Distinct y_category_name from  business, categories  WHERE y_state = '"
                                + state_list.SelectedItem.ToString() + "' AND y_city = '" 
                                + City_list_box.SelectedItem.ToString() 
                                + "' AND y_zipcode = '" + Zipcode_list_box.SelectedItem.ToString() 
                                + "' AND categories.y_business_id = business.y_business_id " 
                                +  " ORDER BY y_category_name";  // + "' AND y_city = '" + City_list_box.SelectedItem.ToString() +
                           //    "' AND y_zipcode = '" + Zipcode_list_box.SelectedItem.ToString() + "' AND business.y_business_id = categories.y_business_id'"*/ // +    "' ORDER BY y_category_name";
                execute_query(sqlStr, addCategory);

                
                sqlStr = "SELECT y_business_name, y_state, y_city, y_zipcode FROM business WHERE y_state = '" + state_list.SelectedItem.ToString() + "' AND y_city = '" + City_list_box.SelectedItem.ToString() + "' AND y_zipcode = '" + Zipcode_list_box.SelectedItem.ToString() + "' ORDER BY y_business_name";
                execute_query(sqlStr, addGridRow);
               

            }

            




        }

        private void Cat_list_box_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {


            business_grid.Items.Clear();
            foreach(var item in Cat_list_box.SelectedItems)
            {

                item.ToString();
                string sqlStr = "SELECT y_business_name, y_state, y_city, y_zipcode FROM business, categories WHERE y_state = '" + state_list.SelectedItem.ToString() + "' AND y_city = '" + City_list_box.SelectedItem.ToString() + "' AND y_zipcode = '" + Zipcode_list_box.SelectedItem.ToString() + "'AND y_category_name = '" + item.ToString() + "' AND categories.y_business_id = business.y_business_id " + " ORDER BY y_business_name";
                execute_query(sqlStr, addGridRow);
            }

        }
    }
}
