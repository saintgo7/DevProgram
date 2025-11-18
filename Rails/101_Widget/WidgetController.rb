class WidgetController < ApplicationController
  before_action :set_widget, only: [:show, :edit, :update, :destroy]

  # GET /widget
  def index
    @widgets = Widget.all
    render json: @widgets
  end

  # GET /widget/1
  def show
    render json: @widget
  end

  # POST /widget
  def create
    @widget = Widget.new(widget_params)

    if @widget.save
      render json: @widget, status: :created
    else
      render json: @widget.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /widget/1
  def update
    if @widget.update(widget_params)
      render json: @widget
    else
      render json: @widget.errors, status: :unprocessable_entity
    end
  end

  # DELETE /widget/1
  def destroy
    @widget.destroy
    head :no_content
  end

  private

  def set_widget
    @widget = Widget.find(params[:id])
  end

  def widget_params
    params.require(:widget).permit(:name)
  end
end
