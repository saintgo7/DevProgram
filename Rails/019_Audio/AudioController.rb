class AudioController < ApplicationController
  before_action :set_audio, only: [:show, :edit, :update, :destroy]

  # GET /audio
  def index
    @audios = Audio.all
    render json: @audios
  end

  # GET /audio/1
  def show
    render json: @audio
  end

  # POST /audio
  def create
    @audio = Audio.new(audio_params)

    if @audio.save
      render json: @audio, status: :created
    else
      render json: @audio.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /audio/1
  def update
    if @audio.update(audio_params)
      render json: @audio
    else
      render json: @audio.errors, status: :unprocessable_entity
    end
  end

  # DELETE /audio/1
  def destroy
    @audio.destroy
    head :no_content
  end

  private

  def set_audio
    @audio = Audio.find(params[:id])
  end

  def audio_params
    params.require(:audio).permit(:name)
  end
end
