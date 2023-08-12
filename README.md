<H1>IoT Gateway for Data Processing and Upload</H1>

<h3>Project Overview</h3>
This project focuses on building an Internet of Things (IoT) system that includes an IoT gateway for efficient communication, data processing, and management between IoT devices and a central cloud-based platform. The project utilizes Amazon Elastic Compute Cloud (Amazon EC2) instances for hosting the IoT gateway, and MQTT (Message Queuing Telemetry Transport) as the messaging protocol for machine-to-machine communication. The MQTT protocol follows a publish/subscribe model, and the project also emphasizes the benefits of this model for decoupling message senders from message receivers.

The project aims to achieve the following key objectives:
<ol>
  <li>
    <b>IoT Gateway:</b> Create a robust IoT gateway that acts as an intermediary between IoT devices, such as sensors and smart devices, and the cloud-based platform or local network.
  </li>
  <li>
    <b>Efficient Data Transmission:</b> Utilize MQTT as the messaging protocol due to its lightweight and efficient nature. MQTT is well-suited for resource-constrained networks with limited bandwidth, making it ideal for IoT data transmission.
  </li>
  <li>
    <b>Reliability and Scalability:</b> Implement MQTT's built-in features to ensure reliability, especially for IoT devices connected over unreliable networks. The protocol's scalability allows it to handle a large number of IoT devices.
  </li>
  <li>
    <b>Security:</b> Leverage modern authentication protocols (e.g., OAuth, TLS1.3) supported by MQTT to ensure secure communication between devices and users.
Automation: Automate the process of data retrieval and upload. Create a scheduled task to periodically run scripts that fetch simulated data and upload it to the cloud.
  </li>
</ol>

<h3>Project Steps</h3>
<ol>
  <li><b>Initial Setup:</b> Created an AWS account and took advantage of the free usage tier for one year. Used a credit card for verification.</li>
  <li><b>EC2 Instance:</b> Created an AWS EC2 instance to host the IoT gateway. The EC2 instance provides resizable computing capacity in the cloud.</li>
  <li><b>InfluxDB Integration:</b> Integrated InfluxDB 2.0 with the EC2 instance for efficient storage of IoT data.</li>
  <li><b>SSH Access:</b> Established SSH access to the EC2 instance using the provided keypair.</li>
  <li><b>Python Environment:</b> Installed the Python interpreter and required Python modules on the EC2 instance..</li>
  <li><b>Uploading Source Code:</b> Created a directory on the EC2 instance to store the source code. Used SCP (Secure Copy Protocol) to import the Python source files to the EC2 instance.</li>
  <li><b>Shell Script:</b> Create a shell script that executes the Python scripts for data retrieval and upload.</li>
  <li><b>Cron Job:</b> Installed and configured cronie on the EC2 instance. Create a cron job to run the shell script daily to automate the data uploading process.</li>
  <li><b>Dashboard Export:</b> Export the generated data to a dashboard in JSON format for visualization and analysis.</li>
</ol>

<h3>Conclusion</h3>
This project combines IoT, Amazon EC2, MQTT, and the publish/subscribe model to build an efficient and reliable IoT system. The focus is on data processing, automation, and secure communication. By following the project timeline and objectives, we aim to create a functional IoT gateway that can handle IoT data efficiently and reliably.