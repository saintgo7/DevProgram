class ChunkController < ApplicationController
  before_action :set_chunk, only: [:show, :edit, :update, :destroy]

  # GET /chunk
  def index
    @chunks = Chunk.all
    render json: @chunks
  end

  # GET /chunk/1
  def show
    render json: @chunk
  end

  # POST /chunk
  def create
    @chunk = Chunk.new(chunk_params)

    if @chunk.save
      render json: @chunk, status: :created
    else
      render json: @chunk.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /chunk/1
  def update
    if @chunk.update(chunk_params)
      render json: @chunk
    else
      render json: @chunk.errors, status: :unprocessable_entity
    end
  end

  # DELETE /chunk/1
  def destroy
    @chunk.destroy
    head :no_content
  end

  private

  def set_chunk
    @chunk = Chunk.find(params[:id])
  end

  def chunk_params
    params.require(:chunk).permit(:name)
  end
end
