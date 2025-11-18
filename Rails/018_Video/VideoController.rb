class VideoController < ApplicationController
  before_action :set_video, only: [:show, :edit, :update, :destroy]

  # GET /video
  def index
    @videos = Video.all
    render json: @videos
  end

  # GET /video/1
  def show
    render json: @video
  end

  # POST /video
  def create
    @video = Video.new(video_params)

    if @video.save
      render json: @video, status: :created
    else
      render json: @video.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /video/1
  def update
    if @video.update(video_params)
      render json: @video
    else
      render json: @video.errors, status: :unprocessable_entity
    end
  end

  # DELETE /video/1
  def destroy
    @video.destroy
    head :no_content
  end

  private

  def set_video
    @video = Video.find(params[:id])
  end

  def video_params
    params.require(:video).permit(:name)
  end
end
