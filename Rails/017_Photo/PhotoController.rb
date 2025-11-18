class PhotoController < ApplicationController
  before_action :set_photo, only: [:show, :edit, :update, :destroy]

  # GET /photo
  def index
    @photos = Photo.all
    render json: @photos
  end

  # GET /photo/1
  def show
    render json: @photo
  end

  # POST /photo
  def create
    @photo = Photo.new(photo_params)

    if @photo.save
      render json: @photo, status: :created
    else
      render json: @photo.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /photo/1
  def update
    if @photo.update(photo_params)
      render json: @photo
    else
      render json: @photo.errors, status: :unprocessable_entity
    end
  end

  # DELETE /photo/1
  def destroy
    @photo.destroy
    head :no_content
  end

  private

  def set_photo
    @photo = Photo.find(params[:id])
  end

  def photo_params
    params.require(:photo).permit(:name)
  end
end
