using System.Collections.ObjectModel;
using Xamarin.Forms;

namespace Program044
{
    public class App : Application
    {
        public App()
        {
            var items = new ObservableCollection<string>();
            for (int i = 1; i <= 30; i++)
                items.Add($"Item {i}");

            var listView = new ListView
            {
                ItemsSource = items,
                RowHeight = 60,
                ItemTemplate = new DataTemplate(() =>
                {
                    var label = new Label
                    {
                        VerticalOptions = LayoutOptions.Center,
                        Margin = new Thickness(15, 0)
                    };
                    label.SetBinding(Label.TextProperty, ".");

                    return new ViewCell
                    {
                        View = new Frame
                        {
                            Margin = new Thickness(10, 5),
                            Padding = new Thickness(10),
                            BackgroundColor = Color.FromHex("#F5F5F5"),
                            Content = label
                        }
                    };
                })
            };

            MainPage = new ContentPage
            {
                Title = "List Demo 044",
                Content = listView
            };
        }
    }
}
