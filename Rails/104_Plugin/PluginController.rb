class PluginController < ApplicationController
  before_action :set_plugin, only: [:show, :edit, :update, :destroy]

  # GET /plugin
  def index
    @plugins = Plugin.all
    render json: @plugins
  end

  # GET /plugin/1
  def show
    render json: @plugin
  end

  # POST /plugin
  def create
    @plugin = Plugin.new(plugin_params)

    if @plugin.save
      render json: @plugin, status: :created
    else
      render json: @plugin.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /plugin/1
  def update
    if @plugin.update(plugin_params)
      render json: @plugin
    else
      render json: @plugin.errors, status: :unprocessable_entity
    end
  end

  # DELETE /plugin/1
  def destroy
    @plugin.destroy
    head :no_content
  end

  private

  def set_plugin
    @plugin = Plugin.find(params[:id])
  end

  def plugin_params
    params.require(:plugin).permit(:name)
  end
end
