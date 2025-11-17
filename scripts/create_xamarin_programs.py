#!/usr/bin/env python3
"""
Create 100 Xamarin programs
"""

import os

base_dir = "/home/user/DevProgram/Xamarin"

# Xamarin program templates
xamarin_programs = {
    1: ("Hello World", "Basic Xamarin.Forms hello world", """using Xamarin.Forms;

namespace Program001
{
    public class App : Application
    {
        public App()
        {
            MainPage = new ContentPage
            {
                Content = new StackLayout
                {
                    VerticalOptions = LayoutOptions.Center,
                    HorizontalOptions = LayoutOptions.Center,
                    Children =
                    {
                        new Label
                        {
                            Text = "Hello, Xamarin!",
                            FontSize = 32,
                            FontAttributes = FontAttributes.Bold,
                            TextColor = Color.Blue,
                            HorizontalTextAlignment = TextAlignment.Center
                        },
                        new Label
                        {
                            Text = "Welcome to Cross-Platform Development",
                            FontSize = 18,
                            TextColor = Color.Gray,
                            HorizontalTextAlignment = TextAlignment.Center,
                            Margin = new Thickness(0, 10, 0, 0)
                        }
                    }
                }
            };
        }
    }
}
"""),

    2: ("Counter App", "Counter with increment/decrement", """using Xamarin.Forms;

namespace Program002
{
    public class App : Application
    {
        private int count = 0;
        private Label countLabel;

        public App()
        {
            countLabel = new Label
            {
                Text = "0",
                FontSize = 72,
                FontAttributes = FontAttributes.Bold,
                TextColor = Color.Blue,
                HorizontalTextAlignment = TextAlignment.Center
            };

            MainPage = new ContentPage
            {
                Content = new StackLayout
                {
                    VerticalOptions = LayoutOptions.Center,
                    HorizontalOptions = LayoutOptions.Center,
                    Spacing = 20,
                    Children =
                    {
                        new Label
                        {
                            Text = "Counter App",
                            FontSize = 32,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        },
                        countLabel,
                        new StackLayout
                        {
                            Orientation = StackOrientation.Horizontal,
                            Spacing = 15,
                            Children =
                            {
                                new Button
                                {
                                    Text = "-",
                                    WidthRequest = 60,
                                    HeightRequest = 60,
                                    BackgroundColor = Color.FromHex("#2196F3"),
                                    TextColor = Color.White,
                                    Command = new Command(() =>
                                    {
                                        count--;
                                        countLabel.Text = count.ToString();
                                    })
                                },
                                new Button
                                {
                                    Text = "Reset",
                                    WidthRequest = 100,
                                    HeightRequest = 60,
                                    BackgroundColor = Color.FromHex("#F44336"),
                                    TextColor = Color.White,
                                    Command = new Command(() =>
                                    {
                                        count = 0;
                                        countLabel.Text = count.ToString();
                                    })
                                },
                                new Button
                                {
                                    Text = "+",
                                    WidthRequest = 60,
                                    HeightRequest = 60,
                                    BackgroundColor = Color.FromHex("#2196F3"),
                                    TextColor = Color.White,
                                    Command = new Command(() =>
                                    {
                                        count++;
                                        countLabel.Text = count.ToString();
                                    })
                                }
                            }
                        }
                    }
                }
            };
        }
    }
}
"""),

    3: ("Todo List", "Xamarin.Forms todo list", """using System.Collections.ObjectModel;
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
"""),

    4: ("Form Input", "Xamarin.Forms form", """using Xamarin.Forms;

namespace Program004
{
    public class App : Application
    {
        private Entry nameEntry;
        private Entry emailEntry;
        private Editor messageEditor;

        public App()
        {
            nameEntry = new Entry
            {
                Placeholder = "Name",
                Margin = new Thickness(10)
            };

            emailEntry = new Entry
            {
                Placeholder = "Email",
                Keyboard = Keyboard.Email,
                Margin = new Thickness(10)
            };

            messageEditor = new Editor
            {
                Placeholder = "Message",
                HeightRequest = 100,
                Margin = new Thickness(10)
            };

            var submitButton = new Button
            {
                Text = "Submit",
                BackgroundColor = Color.FromHex("#2196F3"),
                TextColor = Color.White,
                Margin = new Thickness(10),
                Command = new Command(async () =>
                {
                    if (!string.IsNullOrWhiteSpace(nameEntry.Text) &&
                        !string.IsNullOrWhiteSpace(emailEntry.Text))
                    {
                        await Application.Current.MainPage.DisplayAlert(
                            "Form Submitted",
                            $"Name: {nameEntry.Text}\\nEmail: {emailEntry.Text}",
                            "OK"
                        );
                    }
                })
            };

            MainPage = new ContentPage
            {
                Title = "Form Demo",
                Content = new StackLayout
                {
                    Children =
                    {
                        new Label
                        {
                            Text = "Personal Information",
                            FontSize = 18,
                            FontAttributes = FontAttributes.Bold,
                            Margin = new Thickness(10, 10, 10, 5)
                        },
                        nameEntry,
                        emailEntry,
                        new Label
                        {
                            Text = "Message",
                            FontSize = 18,
                            FontAttributes = FontAttributes.Bold,
                            Margin = new Thickness(10, 10, 10, 5)
                        },
                        messageEditor,
                        submitButton
                    }
                }
            };
        }
    }
}
"""),

    5: ("Navigation", "Xamarin.Forms navigation", """using Xamarin.Forms;

namespace Program005
{
    public class DetailPage : ContentPage
    {
        public DetailPage(string itemName)
        {
            Title = "Details";

            Content = new StackLayout
            {
                VerticalOptions = LayoutOptions.Center,
                HorizontalOptions = LayoutOptions.Center,
                Children =
                {
                    new Label
                    {
                        Text = itemName,
                        FontSize = 32,
                        FontAttributes = FontAttributes.Bold,
                        HorizontalTextAlignment = TextAlignment.Center
                    },
                    new Label
                    {
                        Text = "This is the detail page",
                        FontSize = 18,
                        TextColor = Color.Gray,
                        HorizontalTextAlignment = TextAlignment.Center,
                        Margin = new Thickness(0, 10, 0, 0)
                    }
                }
            };
        }
    }

    public class App : Application
    {
        public App()
        {
            var items = new[] { "Item 1", "Item 2", "Item 3", "Item 4", "Item 5" };

            var listView = new ListView
            {
                ItemsSource = items,
                ItemTemplate = new DataTemplate(() =>
                {
                    var label = new Label
                    {
                        VerticalOptions = LayoutOptions.Center,
                        Margin = new Thickness(10)
                    };
                    label.SetBinding(Label.TextProperty, ".");
                    return new ViewCell { View = label };
                })
            };

            listView.ItemSelected += async (sender, e) =>
            {
                if (e.SelectedItem != null)
                {
                    await (MainPage as NavigationPage)?.PushAsync(
                        new DetailPage(e.SelectedItem.ToString())
                    );
                    listView.SelectedItem = null;
                }
            };

            var mainPage = new ContentPage
            {
                Title = "Items",
                Content = listView
            };

            MainPage = new NavigationPage(mainPage);
        }
    }
}
"""),
}

# Generate remaining programs (6-100)
for i in range(6, 101):
    if i <= 20:
        # Basic UI
        code = f"""using Xamarin.Forms;

namespace Program{i:03d}
{{
    public class App : Application
    {{
        private bool isActive = false;
        private Label statusLabel;

        public App()
        {{
            statusLabel = new Label
            {{
                Text = "Inactive",
                FontSize = 24,
                TextColor = Color.Red,
                HorizontalTextAlignment = TextAlignment.Center
            }};

            MainPage = new ContentPage
            {{
                Content = new StackLayout
                {{
                    VerticalOptions = LayoutOptions.Center,
                    HorizontalOptions = LayoutOptions.Center,
                    Spacing = 20,
                    Children =
                    {{
                        new Label
                        {{
                            Text = "Xamarin Program {i:03d}",
                            FontSize = 28,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        }},
                        statusLabel,
                        new Button
                        {{
                            Text = "Toggle",
                            BackgroundColor = Color.FromHex("#2196F3"),
                            TextColor = Color.White,
                            Command = new Command(() =>
                            {{
                                isActive = !isActive;
                                statusLabel.Text = isActive ? "Active" : "Inactive";
                                statusLabel.TextColor = isActive ? Color.Green : Color.Red;
                            }})
                        }}
                    }}
                }}
            }};
        }}
    }}
}}
"""
    elif i <= 40:
        # State Management
        code = f"""using Xamarin.Forms;

namespace Program{i:03d}
{{
    public class App : Application
    {{
        private int count = 0;
        private bool isChecked = false;
        private Label countLabel;
        private Label checkLabel;

        public App()
        {{
            countLabel = new Label
            {{
                Text = "Count: 0",
                FontSize = 20,
                HorizontalTextAlignment = TextAlignment.Center
            }};

            checkLabel = new Label
            {{
                Text = "Checked: False",
                FontSize = 20,
                HorizontalTextAlignment = TextAlignment.Center
            }};

            MainPage = new ContentPage
            {{
                Content = new StackLayout
                {{
                    VerticalOptions = LayoutOptions.Center,
                    Spacing = 15,
                    Padding = 20,
                    Children =
                    {{
                        new Label
                        {{
                            Text = "State Demo {i:03d}",
                            FontSize = 28,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        }},
                        countLabel,
                        new Button
                        {{
                            Text = "Increment",
                            BackgroundColor = Color.FromHex("#2196F3"),
                            TextColor = Color.White,
                            Command = new Command(() =>
                            {{
                                count++;
                                countLabel.Text = $"Count: {{count}}";
                            }})
                        }},
                        new Switch
                        {{
                            HorizontalOptions = LayoutOptions.Center,
                            OnColor = Color.FromHex("#4CAF50")
                        }}.Bind(Switch.IsToggledProperty, new Binding("IsChecked"))
                            .OnPropertyChanged((s, e) =>
                            {{
                                if (e.PropertyName == "IsToggled")
                                {{
                                    isChecked = (s as Switch).IsToggled;
                                    checkLabel.Text = $"Checked: {{isChecked}}";
                                }}
                            }}),
                        checkLabel
                    }}
                }}
            }};
        }}
    }}
}}
"""
    elif i <= 60:
        # Lists and Collections
        code = f"""using System.Collections.ObjectModel;
using Xamarin.Forms;

namespace Program{i:03d}
{{
    public class App : Application
    {{
        public App()
        {{
            var items = new ObservableCollection<string>();
            for (int i = 1; i <= 30; i++)
                items.Add($"Item {{i}}");

            var listView = new ListView
            {{
                ItemsSource = items,
                RowHeight = 60,
                ItemTemplate = new DataTemplate(() =>
                {{
                    var label = new Label
                    {{
                        VerticalOptions = LayoutOptions.Center,
                        Margin = new Thickness(15, 0)
                    }};
                    label.SetBinding(Label.TextProperty, ".");

                    return new ViewCell
                    {{
                        View = new Frame
                        {{
                            Margin = new Thickness(10, 5),
                            Padding = new Thickness(10),
                            BackgroundColor = Color.FromHex("#F5F5F5"),
                            Content = label
                        }}
                    }};
                }})
            }};

            MainPage = new ContentPage
            {{
                Title = "List Demo {i:03d}",
                Content = listView
            }};
        }}
    }}
}}
"""
    elif i <= 80:
        # Forms and Input
        code = f"""using Xamarin.Forms;

namespace Program{i:03d}
{{
    public class App : Application
    {{
        public App()
        {{
            var entry = new Entry
            {{
                Placeholder = "Enter text",
                Margin = new Thickness(10)
            }};

            var outputLabel = new Label
            {{
                Text = "Text: ",
                FontSize = 18,
                Margin = new Thickness(10)
            }};

            entry.TextChanged += (s, e) =>
            {{
                outputLabel.Text = $"Text: {{e.NewTextValue}}";
            }};

            var slider = new Slider
            {{
                Minimum = 0,
                Maximum = 100,
                Value = 50,
                Margin = new Thickness(10)
            }};

            var sliderLabel = new Label
            {{
                Text = "Value: 50",
                FontSize = 18,
                Margin = new Thickness(10)
            }};

            slider.ValueChanged += (s, e) =>
            {{
                sliderLabel.Text = $"Value: {{(int)e.NewValue}}";
            }};

            MainPage = new ContentPage
            {{
                Title = "Input Demo {i:03d}",
                Content = new StackLayout
                {{
                    Spacing = 10,
                    Children = {{ entry, outputLabel, slider, sliderLabel }}
                }}
            }};
        }}
    }}
}}
"""
    else:
        # Advanced Features
        code = f"""using System;
using Xamarin.Forms;

namespace Program{i:03d}
{{
    public class App : Application
    {{
        public App()
        {{
            var box = new BoxView
            {{
                Color = Color.FromHex("#2196F3"),
                WidthRequest = 100,
                HeightRequest = 100,
                HorizontalOptions = LayoutOptions.Center
            }};

            bool isAnimating = true;
            Device.StartTimer(TimeSpan.FromMilliseconds(16), () =>
            {{
                if (isAnimating)
                {{
                    box.RotateTo(360, 2000);
                    Device.StartTimer(TimeSpan.FromSeconds(2), () =>
                    {{
                        box.Rotation = 0;
                        return false;
                    }});
                }}
                return true;
            }});

            MainPage = new ContentPage
            {{
                Content = new StackLayout
                {{
                    VerticalOptions = LayoutOptions.Center,
                    Spacing = 30,
                    Children =
                    {{
                        new Label
                        {{
                            Text = "Advanced {i:03d}",
                            FontSize = 28,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        }},
                        box,
                        new Button
                        {{
                            Text = "Toggle Animation",
                            BackgroundColor = Color.FromHex("#4CAF50"),
                            TextColor = Color.White,
                            Command = new Command(() =>
                            {{
                                isAnimating = !isAnimating;
                            }})
                        }}
                    }}
                }}
            }};
        }}
    }}
}}
"""

    xamarin_programs[i] = (f"Program {i}", f"Xamarin program {i}", code)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in xamarin_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write App.cs
    with open(f"{program_dir}/App.cs", 'w') as f:
        f.write(code)

    # Create .csproj file
    csproj = f"""<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <ProduceReferenceAssembly>true</ProduceReferenceAssembly>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Xamarin.Forms" Version="5.0.0.2545" />
    <PackageReference Include="Xamarin.Essentials" Version="1.7.5" />
  </ItemGroup>

  <ItemGroup>
    <Compile Include="App.cs" />
  </ItemGroup>
</Project>
"""

    with open(f"{program_dir}/Program{num:03d}.csproj", 'w') as f:
        f.write(csproj)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(xamarin_programs)} Xamarin programs in {base_dir}")
