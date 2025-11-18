class InputController < ApplicationController
  before_action :set_input, only: [:show, :edit, :update, :destroy]

  # GET /input
  def index
    @inputs = Input.all
    render json: @inputs
  end

  # GET /input/1
  def show
    render json: @input
  end

  # POST /input
  def create
    @input = Input.new(input_params)

    if @input.save
      render json: @input, status: :created
    else
      render json: @input.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /input/1
  def update
    if @input.update(input_params)
      render json: @input
    else
      render json: @input.errors, status: :unprocessable_entity
    end
  end

  # DELETE /input/1
  def destroy
    @input.destroy
    head :no_content
  end

  private

  def set_input
    @input = Input.find(params[:id])
  end

  def input_params
    params.require(:input).permit(:name)
  end
end
