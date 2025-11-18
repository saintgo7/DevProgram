class UploadController < ApplicationController
  before_action :set_upload, only: [:show, :edit, :update, :destroy]

  # GET /upload
  def index
    @uploads = Upload.all
    render json: @uploads
  end

  # GET /upload/1
  def show
    render json: @upload
  end

  # POST /upload
  def create
    @upload = Upload.new(upload_params)

    if @upload.save
      render json: @upload, status: :created
    else
      render json: @upload.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /upload/1
  def update
    if @upload.update(upload_params)
      render json: @upload
    else
      render json: @upload.errors, status: :unprocessable_entity
    end
  end

  # DELETE /upload/1
  def destroy
    @upload.destroy
    head :no_content
  end

  private

  def set_upload
    @upload = Upload.find(params[:id])
  end

  def upload_params
    params.require(:upload).permit(:name)
  end
end
