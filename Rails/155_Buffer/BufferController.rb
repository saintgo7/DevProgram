class BufferController < ApplicationController
  before_action :set_buffer, only: [:show, :edit, :update, :destroy]

  # GET /buffer
  def index
    @buffers = Buffer.all
    render json: @buffers
  end

  # GET /buffer/1
  def show
    render json: @buffer
  end

  # POST /buffer
  def create
    @buffer = Buffer.new(buffer_params)

    if @buffer.save
      render json: @buffer, status: :created
    else
      render json: @buffer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /buffer/1
  def update
    if @buffer.update(buffer_params)
      render json: @buffer
    else
      render json: @buffer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /buffer/1
  def destroy
    @buffer.destroy
    head :no_content
  end

  private

  def set_buffer
    @buffer = Buffer.find(params[:id])
  end

  def buffer_params
    params.require(:buffer).permit(:name)
  end
end
