class AlbumController < ApplicationController
  before_action :set_album, only: [:show, :edit, :update, :destroy]

  # GET /album
  def index
    @albums = Album.all
    render json: @albums
  end

  # GET /album/1
  def show
    render json: @album
  end

  # POST /album
  def create
    @album = Album.new(album_params)

    if @album.save
      render json: @album, status: :created
    else
      render json: @album.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /album/1
  def update
    if @album.update(album_params)
      render json: @album
    else
      render json: @album.errors, status: :unprocessable_entity
    end
  end

  # DELETE /album/1
  def destroy
    @album.destroy
    head :no_content
  end

  private

  def set_album
    @album = Album.find(params[:id])
  end

  def album_params
    params.require(:album).permit(:name)
  end
end
