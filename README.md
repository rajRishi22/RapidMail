# RapidMail

RapidMail is a simple web application that allows users to send emails using a web interface. It is built using Flask and can be deployed easily on platforms like Vercel.

## Table of Contents
- [Preview](#Preview)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Preview 
![image](https://github.com/user-attachments/assets/8e4d1c3c-832d-45c2-991e-306539dc83d0)
![image](https://github.com/user-attachments/assets/f2d10b6d-f74c-4ffa-b059-97d7c8d871bb)
![image](https://github.com/user-attachments/assets/8ce6accb-4ee4-4bba-bcb1-6b195cf36fa1)
![image](https://github.com/user-attachments/assets/05ae4475-95dc-4fd1-a499-4cc2af53ba1f)




## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/rajRishi22/RapidMail.git
    cd RapidMail
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

5. **Open your browser and visit:**
    ```
    http://127.0.0.1:5000
    ```

## Usage

- Navigate to the home page and fill out the email form.
- Click on the "Send" button to send the email.
- You can also navigate to the "How to Use" page for detailed instructions.

## Deployment

### Deploying on Vercel

1. **Sign Up and Install Vercel CLI:**
    - Go to [Vercel](https://vercel.com/) and sign up for a free account.
    - Install the Vercel CLI:
      ```bash
      npm install -g vercel
      ```

2. **Prepare Your Application:**
    Ensure your application has the following files:

    **vercel.json:**
    ```json
    {
      "builds": [
        { "src": "app.py", "use": "@vercel/python" }
      ],
      "routes": [
        { "src": "/(.*)", "dest": "app.py" }
      ]
    }
    ```

3. **Deploy Your Application:**
    - Navigate to your project directory in the terminal.
    - Run the following command to deploy your project:
      ```bash
      vercel
      ```
    - Follow the prompts to link your project to Vercel and deploy.

4. **Access Your Application:**
    - After deployment, Vercel will provide a URL where your application is hosted.
    - Open the provided URL to access your deployed application.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact:
- Raj Rishi: rishiraj.dev1234@gmail.com
- GitHub: [rajRishi22](https://github.com/rajRishi22)
