class StyleController < ApplicationController
  before_action :set_style, only: [:show, :edit, :update, :destroy]

  # GET /style
  def index
    @styles = Style.all
    render json: @styles
  end

  # GET /style/1
  def show
    render json: @style
  end

  # POST /style
  def create
    @style = Style.new(style_params)

    if @style.save
      render json: @style, status: :created
    else
      render json: @style.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /style/1
  def update
    if @style.update(style_params)
      render json: @style
    else
      render json: @style.errors, status: :unprocessable_entity
    end
  end

  # DELETE /style/1
  def destroy
    @style.destroy
    head :no_content
  end

  private

  def set_style
    @style = Style.find(params[:id])
  end

  def style_params
    params.require(:style).permit(:name)
  end
end
