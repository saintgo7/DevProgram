class DownloadController < ApplicationController
  before_action :set_download, only: [:show, :edit, :update, :destroy]

  # GET /download
  def index
    @downloads = Download.all
    render json: @downloads
  end

  # GET /download/1
  def show
    render json: @download
  end

  # POST /download
  def create
    @download = Download.new(download_params)

    if @download.save
      render json: @download, status: :created
    else
      render json: @download.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /download/1
  def update
    if @download.update(download_params)
      render json: @download
    else
      render json: @download.errors, status: :unprocessable_entity
    end
  end

  # DELETE /download/1
  def destroy
    @download.destroy
    head :no_content
  end

  private

  def set_download
    @download = Download.find(params[:id])
  end

  def download_params
    params.require(:download).permit(:name)
  end
end
