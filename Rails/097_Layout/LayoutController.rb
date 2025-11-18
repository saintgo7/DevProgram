class LayoutController < ApplicationController
  before_action :set_layout, only: [:show, :edit, :update, :destroy]

  # GET /layout
  def index
    @layouts = Layout.all
    render json: @layouts
  end

  # GET /layout/1
  def show
    render json: @layout
  end

  # POST /layout
  def create
    @layout = Layout.new(layout_params)

    if @layout.save
      render json: @layout, status: :created
    else
      render json: @layout.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /layout/1
  def update
    if @layout.update(layout_params)
      render json: @layout
    else
      render json: @layout.errors, status: :unprocessable_entity
    end
  end

  # DELETE /layout/1
  def destroy
    @layout.destroy
    head :no_content
  end

  private

  def set_layout
    @layout = Layout.find(params[:id])
  end

  def layout_params
    params.require(:layout).permit(:name)
  end
end
