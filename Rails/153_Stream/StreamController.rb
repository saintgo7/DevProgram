class StreamController < ApplicationController
  before_action :set_stream, only: [:show, :edit, :update, :destroy]

  # GET /stream
  def index
    @streams = Stream.all
    render json: @streams
  end

  # GET /stream/1
  def show
    render json: @stream
  end

  # POST /stream
  def create
    @stream = Stream.new(stream_params)

    if @stream.save
      render json: @stream, status: :created
    else
      render json: @stream.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /stream/1
  def update
    if @stream.update(stream_params)
      render json: @stream
    else
      render json: @stream.errors, status: :unprocessable_entity
    end
  end

  # DELETE /stream/1
  def destroy
    @stream.destroy
    head :no_content
  end

  private

  def set_stream
    @stream = Stream.find(params[:id])
  end

  def stream_params
    params.require(:stream).permit(:name)
  end
end
