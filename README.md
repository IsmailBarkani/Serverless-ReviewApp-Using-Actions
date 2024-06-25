
<a name="readme-top"></a>




<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Serverless ReviewApp using Actions</h3>

  <p align="center">
    Automate serverless deployment using actions
  </p>
</div>





<!-- ABOUT THE PROJECT -->
## About The Project
This project aims to demonstrate the use of GitHub Actions to ensure seamless and independent deployment of your serverless application associated with your PR. The action is triggered whenever a PR is raised, creating a dedicated testing environment for the changes. This mirrors the ReviewApp technology present in GitLab.

The project comprises a simple, fully serverless REST API composed of an AWS Lambda integrated with an AWS API Gateway. CloudFormation is used to manage these resources as code.

A workflow is created to execute multiple stages of CI/CD, including building and testing the API, deploying it into AWS, and providing the API URL and invocation information.




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
