using System.Collections.ObjectModel;
using Xamarin.Forms;

namespace Program003
{
    public class App : Application
    {
        private ObservableCollection<string> tasks = new ObservableCollection<string>();
        private Entry taskEntry;
        private ListView listView;

        public App()
        {
            taskEntry = new Entry
            {
                Placeholder = "Enter task",
                Margin = new Thickness(10, 10, 10, 0)
            };

            var addButton = new Button
            {
                Text = "Add",
                BackgroundColor = Color.FromHex("#2196F3"),
                TextColor = Color.White,
                Margin = new Thickness(10, 5, 10, 10),
                Command = new Command(() =>
                {
                    if (!string.IsNullOrWhiteSpace(taskEntry.Text))
                    {
                        tasks.Add(taskEntry.Text);
                        taskEntry.Text = string.Empty;
                    }
                })
            };

            listView = new ListView
            {
                ItemsSource = tasks,
                ItemTemplate = new DataTemplate(() =>
                {
                    var label = new Label
                    {
                        VerticalOptions = LayoutOptions.Center,
                        Margin = new Thickness(10, 0, 0, 0)
                    };
                    label.SetBinding(Label.TextProperty, ".");

                    var deleteButton = new Button
                    {
                        Text = "✕",
                        BackgroundColor = Color.FromHex("#F44336"),
                        TextColor = Color.White,
                        WidthRequest = 50
                    };

                    var stackLayout = new StackLayout
                    {
                        Orientation = StackOrientation.Horizontal,
                        Children = { label, deleteButton }
                    };

                    deleteButton.Clicked += (s, e) =>
                    {
                        var item = (s as Button)?.BindingContext as string;
                        if (item != null)
                            tasks.Remove(item);
                    };

                    return new ViewCell { View = stackLayout };
                })
            };

            var emptyLabel = new Label
            {
                Text = "No tasks yet. Add one above!",
                TextColor = Color.Gray,
                HorizontalTextAlignment = TextAlignment.Center,
                Margin = new Thickness(0, 20, 0, 0)
            };

            tasks.CollectionChanged += (s, e) =>
            {
                emptyLabel.IsVisible = tasks.Count == 0;
            };
            emptyLabel.IsVisible = true;

            MainPage = new ContentPage
            {
                Title = "Todo List",
                Content = new StackLayout
                {
                    Children = { taskEntry, addButton, listView, emptyLabel }
                }
            };
        }
    }
}
