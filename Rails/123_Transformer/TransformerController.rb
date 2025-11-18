class TransformerController < ApplicationController
  before_action :set_transformer, only: [:show, :edit, :update, :destroy]

  # GET /transformer
  def index
    @transformers = Transformer.all
    render json: @transformers
  end

  # GET /transformer/1
  def show
    render json: @transformer
  end

  # POST /transformer
  def create
    @transformer = Transformer.new(transformer_params)

    if @transformer.save
      render json: @transformer, status: :created
    else
      render json: @transformer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /transformer/1
  def update
    if @transformer.update(transformer_params)
      render json: @transformer
    else
      render json: @transformer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /transformer/1
  def destroy
    @transformer.destroy
    head :no_content
  end

  private

  def set_transformer
    @transformer = Transformer.find(params[:id])
  end

  def transformer_params
    params.require(:transformer).permit(:name)
  end
end
