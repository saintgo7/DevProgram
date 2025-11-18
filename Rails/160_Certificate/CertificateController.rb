class CertificateController < ApplicationController
  before_action :set_certificate, only: [:show, :edit, :update, :destroy]

  # GET /certificate
  def index
    @certificates = Certificate.all
    render json: @certificates
  end

  # GET /certificate/1
  def show
    render json: @certificate
  end

  # POST /certificate
  def create
    @certificate = Certificate.new(certificate_params)

    if @certificate.save
      render json: @certificate, status: :created
    else
      render json: @certificate.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /certificate/1
  def update
    if @certificate.update(certificate_params)
      render json: @certificate
    else
      render json: @certificate.errors, status: :unprocessable_entity
    end
  end

  # DELETE /certificate/1
  def destroy
    @certificate.destroy
    head :no_content
  end

  private

  def set_certificate
    @certificate = Certificate.find(params[:id])
  end

  def certificate_params
    params.require(:certificate).permit(:name)
  end
end
