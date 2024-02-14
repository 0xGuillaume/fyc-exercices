terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
      version = "2.4.1"
    }
    aws = {
      source = "hashicorp/aws"
      version = "5.36.0"
    }
  }
}

# 1. Création du fichier
resource "local_file" "fyc" {
  content  = "Partons à la découverte de Terraform !"
  filename = "${path.module}/fyc.txt"
}

# 2. Création du bucket S3
resource "aws_s3_bucket" "fycbucket" {
  # Penser à modifier le nom du bucket, qui doit être unique.
  bucket = "fyc-bucket-hands-on-2"

  tags = {
    Name        = "FycBucket"
  }
}

# 3. Upload du fichier dans le bucket S3
resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.fycbucket.id
  key    = "fyc.txt"
  source = local_file.fyc.filename
}
